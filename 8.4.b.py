# Elements of Causal Inference
# Solution to Problem 8.4.b
import numpy as np
import scipy.stats


np.random.seed(42)
sample_size = 200
N_Y = np.random.normal(loc=0.0,scale=1.0,size=sample_size)
N_Z = np.random.normal(loc=0.0,scale=1.0,size=sample_size)
Z = N_Z
Y = np.square(Z) + N_Z

p = scipy.stats.norm(0, 1).pdf(Z)
p_tilde = scipy.stats.norm(2, 1).pdf(Z)

values = Y * p_tilde / p
xi = np.mean(values)
print(xi)
