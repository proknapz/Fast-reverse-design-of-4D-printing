This is a project for the fast reverse design of 4D-printed voxelized composite structures.


Commands to run:
py -3.8 -m venv .venv

run this if ps1 does not work.
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

.\.venv\Scripts\Activate.ps1  

python -m pip install --upgrade pip
python -m pip install tensorflow==2.10.1
python -m pip install numpy matplotlib pandas

python -c "import numpy, pandas, matplotlib, tensorflow; print('All imports successful'); print('TensorFlow:', tensorflow.__version__)"


Test the actual script:
python ".\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py"

python ".\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py"
2026-09-28 12:10:50.001295: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'cudart64_110.dll'; dlerror: cudart64_110.dll not found
2026-09-28 12:10:50.001433: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:171: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv1_0 = tf.layers.conv1d(inputs=x_cut[0], filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:173: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv1_1 = tf.layers.conv1d(inputs=x_cut[1], filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:175: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv1_2 = tf.layers.conv1d(inputs=x_cut[2], filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:177: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv1_3 = tf.layers.conv1d(inputs=x_cut[3], filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:179: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv1_4 = tf.layers.conv1d(inputs=x_cut[4], filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:181: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv1_5 = tf.layers.conv1d(inputs=x_cut[5], filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:183: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv1_6 = tf.layers.conv1d(inputs=x_cut[6], filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:185: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv1_7 = tf.layers.conv1d(inputs=x_cut[7], filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:187: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv1_8 = tf.layers.conv1d(inputs=x_cut[8], filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:189: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv1_9 = tf.layers.conv1d(inputs=x_cut[9], filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:196: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv2_0 = tf.layers.conv1d(inputs=x0, filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:198: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv2_1 = tf.layers.conv1d(inputs=conv2_0 + x1, filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:200: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv2_2 = tf.layers.conv1d(inputs=conv2_1 + x2, filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:202: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv2_3 = tf.layers.conv1d(inputs=conv2_2 + x3, filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:204: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv2_4 = tf.layers.conv1d(inputs=conv2_3 + x4, filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:206: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv2_5 = tf.layers.conv1d(inputs=conv2_4 + x5, filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:208: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv2_6 = tf.layers.conv1d(inputs=conv2_5 + x6, filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:210: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv2_7 = tf.layers.conv1d(inputs=conv2_6 + x7, filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:212: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv2_8 = tf.layers.conv1d(inputs=conv2_7 + x8, filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:214: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv2_9 = tf.layers.conv1d(inputs=conv2_8 + x9, filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:220: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv3_0 = tf.layers.conv1d(inputs=x0, filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:222: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv3_1 = tf.layers.conv1d(inputs=conv3_0 + x1, filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:224: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv3_2 = tf.layers.conv1d(inputs=conv3_1 + x2, filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:226: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv3_3 = tf.layers.conv1d(inputs=conv3_2 + x3, filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:228: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv3_4 = tf.layers.conv1d(inputs=conv3_3 + x4, filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:230: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv3_5 = tf.layers.conv1d(inputs=conv3_4 + x5, filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:232: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv3_6 = tf.layers.conv1d(inputs=conv3_5 + x6, filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:234: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv3_7 = tf.layers.conv1d(inputs=conv3_6 + x7, filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:236: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv3_8 = tf.layers.conv1d(inputs=conv3_7 + x8, filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:238: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  conv3_9 = tf.layers.conv1d(inputs=conv3_8 + x9, filters=filter, kernel_size=3, padding='same')
.\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py:255: UserWarning: `tf.layers.conv1d` is deprecated and will be removed in a future version. Please Use `tf.keras.layers.Conv1D` instead.
  Net4_output = tf.layers.conv1d(inputs=Net3_output, filters=200, kernel_size=3, padding='same')
2026-09-28 12:10:54.046419: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX AVX2
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2026-09-28 12:10:54.050000: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'nvcuda.dll'; dlerror: nvcuda.dll not found
2026-09-28 12:10:54.050110: W tensorflow/stream_executor/cuda/cuda_driver.cc:263] failed call to cuInit: UNKNOWN ERROR (303)
2026-09-28 12:10:54.058158: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:169] retrieving CUDA diagnostic information for host: DESKTOP-3J2FG8E
2026-09-28 12:10:54.058437: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:176] hostname: DESKTOP-3J2FG8E
2026-09-28 12:10:54.073729: I tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc:354] MLIR V1 optimization pass is not enabled
$$$$$$$$$$$$$$$$-------frequency------$$$$$$$$$$$$$--------------------------------- 0
====================================generation===================================:0
====================================generation===================================:1
====================================generation===================================:2
====================================generation===================================:3
====================================generation===================================:4
--------generation:4-----number:41
Traceback (most recent call last):
  File ".\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py", line 334, in <module>
    with open(csv_file_path, 'a', newline='') as file:
FileNotFoundError: [Errno 2] No such file or directory: './PEA_total_gen/PEA_total_gen_mutate0.55.csv'


since you got this error: 
mkdir .\PEA_total_gen
mkdir .\PEA_design_time

python ".\Code_of_PEA_and_Traditional_EA\PEA_for_reverse_design.py" change iterations to 10

after check 
PEA_total_gen_mutate0.55.csv
PEA_time_mutate0.55.csv  

Successfully reproduced the Wang et al. fast reverse-design implementation using Python 3.8.10 and TensorFlow 2.10.1. The pretrained SEP-CNN model loaded successfully, and the PEA reverse-design algorithm completed a 10-generation test run without runtime errors. The generated PEA_total_gen_mutate0.55.csv and PEA_time_mutate0.55.csv files were used to verify the optimization and timing outputs.