This is a project for the fast reverse design of 4D-printed voxelized composite structures.

# Photo-to-splint web demo

A **demonstration** Flask app: upload a photo of a hand, estimate a 3D point cloud, and generate a parametric wrist-to-palm splint (orthosis) for 3D viewing and STL/PLY download.

**This is a demonstration only. It is not medical-grade, not a medical device, and not for diagnosis, treatment, or clinical use.** Geometry comes from a single 2D photo plus an assumed hand length, so it is approximate.

## What it does

1. **Upload** a JPG/PNG (max 10 MB).
2. **MediaPipe Hands** finds 21 landmarks and a convex-hull hand mask.
3. **Depth Anything V2 Small** (CPU, via Hugging Face `transformers`) estimates a depth map. If that fails, **MiDaS small** via `torch.hub` is used.
4. Masked pixels are **back-projected** to 3D, **scaled** so wrist → middle fingertip matches the entered hand length (default 18 cm), then cleaned with **Open3D** (voxel downsample, statistical outlier removal, normals). Exported as `cloud.ply`.
5. A **parametric shell** (dorsal or volar) is offset **3 mm** from the surface with **2 mm** thickness, cut from the wrist to the finger bases (optional PIP / finger-extension), with strap slots, and exported as `splint.stl`.
6. The page shows both in a **Three.js** viewer (OrbitControls, PLY + STL loaders).

Photograph the **same side** of the hand as the splint type (dorsal photo for a dorsal splint).

## Project layout

```
app.py                 Flask routes (POST /upload)
pipeline/
  landmarks.py         MediaPipe landmarks + mask
  depth.py             Depth Anything / MiDaS
  pointcloud.py        Back-project, scale, Open3D cleanup
  splint.py            Parametric shell → STL
static/                CSS + Three.js viewer
templates/index.html
tests/                 pytest + sample PNG
uploads/  outputs/     runtime files
```

## Requirements (Windows, CPU)

Use **64-bit Python 3.8 or newer**. The pinned MediaPipe 0.10.11 release has a Windows CPython 3.8 wheel; newer MediaPipe releases may use Python 3.9+ type annotation syntax. The first run may download `hand_landmarker.task` and the depth weights.

```bat
cd C:\Users\Dell\Documents\GitHub\Fast-reverse-design-of-4D-printing
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The first depth run downloads **Depth Anything V2 Small** (Hugging Face). That needs a network connection and some disk space. Everything is intended to run on **CPU** (slow is OK).

If you only want this demo and not the rest of the research stack, install:

```bat
  pip install flask pillow numpy scipy opencv-python-headless mediapipe==0.10.11 transformers open3d trimesh pytest
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

(`tensorflow` in `requirements.txt` is for the original reverse-design code, not this demo.)

## Run

```bat
.venv\Scripts\activate
set FLASK_APP=app.py
flask run
```

Open http://127.0.0.1:5000

PowerShell equivalent:

```powershell
$env:FLASK_APP = "app.py"
flask run
```

Or: `python app.py`

## Tests

```bat
pytest tests/test_pipeline.py -q
```

The sample image (`tests/data/sample_hand.png`) has **no hand**, so the test checks the clear **“No hand detected”** error. Splint/point-cloud tests use a synthetic 3D patch so they do not download depth models.

To try a real photo: use a well-lit picture of one hand, palm or dorsum facing the camera, fingers spread, and set hand length in centimetres.

## API

`POST /upload` (multipart):

| field | meaning |
| --- | --- |
| `photo` | JPG or PNG |
| `hand_length_cm` | default `18` |
| `side` | `dorsal` (default) or `volar` |
| `finger_extension` | `true` / `false` |

JSON on success:

```json
{
  "cloud_url": "/outputs/<id>/cloud.ply",
  "splint_url": "/outputs/<id>/splint.stl",
  "landmarks_url": "/outputs/<id>/landmarks.json"
}
```
