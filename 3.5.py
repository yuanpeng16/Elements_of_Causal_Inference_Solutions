# Elements of Causal Inference
# Solution to Problem 3.5
import numpy as np


np.random.seed(42)
sample_size = 200
N_X = np.random.normal(loc=0.0,scale=1.0,size=sample_size)
N_Y = np.random.normal(loc=0.0,scale=1.0,size=sample_size)
Y = N_Y
X = np.square(Y) + N_X
print(X)
