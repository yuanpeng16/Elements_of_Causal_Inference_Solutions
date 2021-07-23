# Elements of Causal Inference
# Solution to Problem 6.55.c
import numpy as np


np.random.seed(42)
sample_size = 200
alpha = 2

def get_normal(samples):
    return np.random.normal(loc=0.0,scale=1.0,size=samples)


N_V = get_normal(sample_size)
N_W = get_normal(sample_size)
N_Y = get_normal(sample_size)
N_Z = get_normal(sample_size)

V = N_V
X = np.array([3] * sample_size)
Y = -X + N_Y
Z = alpha * X + N_Z
W = -2 * V + 3 * Y + 5 * Z + N_W

for x, w in zip(X, W):
    print(x, w)

