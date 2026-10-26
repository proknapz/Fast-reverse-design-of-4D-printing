"""Flask demo: upload a hand photo, preview the point cloud and splint."""

from __future__ import annotations

import uuid
import traceback
from pathlib import Path

from flask import Flask, jsonify, render_template, request, send_from_directory
from PIL import Image, UnidentifiedImageError
from werkzeug.datastructures import FileStorage

from pipeline import HandNotDetectedError, PipelineError, run_pipeline

ROOT = Path(__file__).resolve().parent
UPLOAD_DIR = ROOT / "uploads"
OUTPUT_DIR = ROOT / "outputs"
ALLOWED_FORMATS = {"JPEG", "PNG"}
ALLOWED_EXT = {".jpg", ".jpeg", ".png"}
MAX_BYTES = 10 * 1024 * 1024

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config["MAX_CONTENT_LENGTH"] = MAX_BYTES


def _ensure_dirs() -> None:
    UPLOAD_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)


def _validate_image(file: FileStorage) -> str:
    if file is None or not file.filename:
        raise PipelineError("Please choose a JPG or PNG photo.")
    suffix = Path(file.filename).suffix.lower()
    if suffix not in ALLOWED_EXT:
        raise PipelineError("File type not allowed. Upload a JPG or PNG image.")
    data = file.read()
    file.seek(0)
    if len(data) > MAX_BYTES:
        raise PipelineError("File is too large. Maximum size is 10 MB.")
    if len(data) < 32:
        raise PipelineError("The uploaded file is empty or invalid.")
    try:
        with Image.open(file.stream) as img:
            fmt = (img.format or "").upper()
            img.verify()
    except (UnidentifiedImageError, OSError) as exc:
        raise PipelineError("Could not read the image. Upload a valid JPG or PNG.") from exc
    file.stream.seek(0)
    if fmt not in ALLOWED_FORMATS:
        raise PipelineError("File type not allowed. Upload a JPG or PNG image.")
    return suffix if suffix != ".jpeg" else ".jpg"


@app.errorhandler(413)
def too_large(_err):
    return jsonify({"error": "File is too large. Maximum size is 10 MB."}), 413


@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    _ensure_dirs()
    try:
        image_file = request.files.get("photo")
        suffix = _validate_image(image_file)

        hand_length_cm = float(request.form.get("hand_length_cm", 18))
        side = request.form.get("side", "dorsal").strip().lower()
        finger_extension = request.form.get("finger_extension", "false").lower() in {
            "1",
            "true",
            "on",
            "yes",
        }

        job_id = uuid.uuid4().hex
        upload_path = UPLOAD_DIR / f"{job_id}{suffix}"
        image_file.save(upload_path)
        job_dir = OUTPUT_DIR / job_id
        result = run_pipeline(
            str(upload_path),
            str(job_dir),
            hand_length_cm=hand_length_cm,
            side=side,  # type: ignore[arg-type]
            finger_extension=finger_extension,
        )
        return jsonify(
            {
                "job_id": job_id,
                "cloud_url": f"/outputs/{job_id}/cloud.ply",
                "splint_url": f"/outputs/{job_id}/splint.stl",
                "landmarks_url": f"/outputs/{job_id}/landmarks.json",
                "point_count": result["meta"]["point_count"],
                "splint_watertight": result["meta"]["splint_watertight"],
            }
        )
    except HandNotDetectedError as exc:
        return jsonify({"error": str(exc)}), 400
    except PipelineError as exc:
        return jsonify({"error": str(exc)}), 400
    except ValueError:
        return jsonify({"error": "Hand length must be a number (centimetres)."}), 400
    except Exception as exc:
        error_trace = traceback.format_exc()
        # Some embedded Windows Python consoles have invalid stdout/stderr
        # handles. Logging must not replace the original pipeline exception.
        try:
            app.logger.error("Unexpected pipeline failure\n%s", error_trace)
        except OSError:
            pass
        return jsonify(
            {
                "error": f"Processing failed: {str(exc)}",
                "traceback": error_trace,
            }
        ), 500


@app.route("/outputs/<job_id>/<filename>")
def outputs(job_id: str, filename: str):
    if filename not in {"cloud.ply", "splint.stl", "landmarks.json"}:
        return jsonify({"error": "Unknown output file."}), 404
    folder = OUTPUT_DIR / job_id
    if not (folder / filename).is_file():
        return jsonify({"error": "Output not found."}), 404
    return send_from_directory(folder, filename, as_attachment=False)


if __name__ == "__main__":
    _ensure_dirs()
    app.run(debug=True)
