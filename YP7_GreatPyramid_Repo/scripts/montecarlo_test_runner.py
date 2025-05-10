# Runs Monte Carlo simulations
import numpy as np
def monte_carlo(sequence, skip, runs=100000):
    return [np.random.permutation(sequence) for _ in range(runs)]
