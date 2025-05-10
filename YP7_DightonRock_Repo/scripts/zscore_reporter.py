# Calculates Z-score and p-value
from scipy.stats import norm
def calculate_z(obs, mean, std):
    z = (obs - mean) / std
    p = 1 - norm.cdf(z)
    return z, p
