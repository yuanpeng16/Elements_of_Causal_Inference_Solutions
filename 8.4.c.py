# Elements of Causal Inference
# Solution to Problem 8.4.b
import numpy as np
import scipy.stats


np.random.seed(42)
p = scipy.stats.norm(0, 1)
p_tilde = scipy.stats.norm(2, 1)


def experiment(n):
    sample_size = n
    N_Y = np.random.normal(loc=0.0,scale=1.0,size=sample_size)
    N_Z = np.random.normal(loc=0.0,scale=1.0,size=sample_size)
    Z = N_Z
    Y = np.square(Z) + N_Z

    w = p_tilde.pdf(Z) / p.pdf(Z)
    values = Y * w
    xi = np.mean(values)
    variance = np.var(w)
    return xi, variance

for n in [5, 50, 500, 5000, 50000]:
    xi, variance = experiment(n)
    print(n, xi, variance)

