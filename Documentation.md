We should inspect Wang's original network first, then design the ResNet around the same input/output contract.

The original Wang model expects:

2 × 10

which means 20 values at its model input, while your CSV has 10 design values.

The reason this works in Wang's code is that the PEA's 2 × 10 representation is part of the evolutionary representation, and the model's internal processing needs to be examined to determine exactly how those values correspond to the 10 design variables.


go to CNN_Train.py and get the shapes of each layer

        2 × 10
          │
          ▼
       CNN
          │
          ▼
        2 × 200


( batch, 2, 10 )
       ↓
Conv1D 320
       ↓
( batch, 2, 320 )
       ↓
Conv1D 320
       ↓
( batch, 2, 320 )
       ↓
Conv1D 320
       ↓
( batch, 2, 320 )
       ↓
Conv1D 200
       ↓
( batch, 2, 200 )



input is only 2×10.

write the 2D ResNet training version of cnn_train.py while preserving Wang's:

data loading
(2,10) input
(2,200) output
/1000 scaling
Curve_unification
train/test split
TensorFlow 2.10 / TF1-compatible style


project becomes
                 Wang Dataset
                      │
                      ▼
                10 variables
                      │
              pair 2 rows together
                      │
                      ▼
                  2 × 10
                      │
                      ▼
              ┌──────────────┐
              │  2D ResNet   │
              └──────┬───────┘
                     │
                     ▼
                  2 × 200
                     │
                     ▼
              predicted curve



after running PEA for reverse design for both models 
compare the PEA_design_time and 


changed model in PEA_for_reverse_design to load the resnet model and go through a new cnn



after running  python .\Code_DL_model_prediction\train_resnet_fair.py
output
Train inputs: (6000, 2, 10)
Train outputs: (6000, 2, 200)
Test inputs: (2000, 2, 10)
Test outputs: (2000, 2, 200)

Step 500/10000 - Training MSE: 0.0017630126094445586
Step 1000/10000 - Training MSE: 0.0005269658286124468
Step 1500/10000 - Training MSE: 0.000334757671225816
Step 2000/10000 - Training MSE: 0.00025376741541549563
Step 2500/10000 - Training MSE: 0.00020919223607052118
Step 3000/10000 - Training MSE: 0.00020660074369516224
Step 3500/10000 - Training MSE: 0.0001975956402020529
Step 4000/10000 - Training MSE: 0.00011772762081818655
Step 4500/10000 - Training MSE: 0.00013570222654379904
Step 5000/10000 - Training MSE: 7.684298179810867e-05
Step 5500/10000 - Training MSE: 0.00012205734674353153
Step 6000/10000 - Training MSE: 7.272041693795472e-05
Step 6500/10000 - Training MSE: 6.952779222046956e-05
Step 7000/10000 - Training MSE: 0.00011085884761996567
Step 7500/10000 - Training MSE: 9.395582310389727e-05
Step 8000/10000 - Training MSE: 8.376217010663822e-05
Step 8500/10000 - Training MSE: 5.1803777751047164e-05
Step 9000/10000 - Training MSE: 5.56357299501542e-05
Step 9500/10000 - Training MSE: 5.572723239311017e-05
Step 10000/10000 - Training MSE: 6.648951239185408e-05

========================================
2D RESNET FAIR TRAINING RESULTS
========================================
Training steps: 10000
Test samples: 2000
Test MSE: 5.5905177e-05
========================================

Model saved to: ./model_weights_2D_ResNet_fair

python .\Code_DL_model_prediction\train_sepcnn_fair.py

========================================
SEP-CNN FAIR TRAINING RESULTS
========================================
Training steps: 10000
Test samples: 2000
Test MSE: 0.0022869948
========================================

Step 500/10000 - Training MSE: 0.03569081053137779
Step 1000/10000 - Training MSE: 0.015467173419892788
Step 1500/10000 - Training MSE: 0.009645983576774597
Step 2000/10000 - Training MSE: 0.007364819757640362
Step 2500/10000 - Training MSE: 0.006622928660362959
Step 3000/10000 - Training MSE: 0.008834278210997581
Step 3500/10000 - Training MSE: 0.008116338402032852
Step 4000/10000 - Training MSE: 0.005350393708795309
Step 4500/10000 - Training MSE: 0.004071924369782209
Step 5000/10000 - Training MSE: 0.0037082440685480833
Step 5500/10000 - Training MSE: 0.004688166081905365
Step 6000/10000 - Training MSE: 0.002593549434095621
Step 6500/10000 - Training MSE: 0.003865926992148161
Step 7000/10000 - Training MSE: 0.0038141750264912844
Step 7500/10000 - Training MSE: 0.002726334147155285
Step 8000/10000 - Training MSE: 0.003789616050198674
Step 8500/10000 - Training MSE: 0.0030758948996663094
Step 9000/10000 - Training MSE: 0.002720039337873459
Step 9500/10000 - Training MSE: 0.002371744252741337
Step 10000/10000 - Training MSE: 0.0018985497299581766


Under a controlled training experiment using the same 10,000 optimizer steps, batch size, learning rate, preprocessing, and MSE objective, the 2D ResNet achieved a test MSE of 5.59 × 10⁻⁵, compared with 2.29 × 10⁻³ for the SEP-CNN. Thus, the ResNet achieved a substantially lower test MSE under the controlled training budget.


python .\Code_of_PEA_and_Traditional_EA\PEA_fair_resnet.py


python ./Code_of_PEA_and_Traditional_EA/PEA_fair_sepcnn_instrumented.py
python ./Code_of_PEA_and_Traditional_EA/PEA_fair_resnet_instrumented.py

The repeated generation-5 result is caused by the deterministic structure of the PEA's final search, not by duplicate candidates or a collapsed population.

You have experimentally verified:

1,024 candidates
1,024 unique candidates
exactly 1 unique prefix
same winning candidate index
same result across 10 runs

for both archectectures



from inspecting PEA_gen5

ResNet produces a much better minimum within the searched design space, while the average prediction error across the 1,024 candidates is similar to SEP-CNN.

The PEA itself is deterministic at generation 5


We performed a controlled 2×2 cross-model experiment to separate the effects of the candidate design and the learned forward model. The results showed a strong interaction between the two: neither model consistently produced lower prediction error across both designs. This indicates that both the selected 4D-printing configuration and the forward model influence the predicted shape error."

herefore, we do not interpret the lower original ResNet PEA error as evidence that ResNet is universally superior. Instead, the results motivate evaluating forward models across a common set of candidate designs

model-by-design interaction rather than a universally superior forward model.

hromosome represents:

a candidate material/structural configuration for the 4D-printed structur