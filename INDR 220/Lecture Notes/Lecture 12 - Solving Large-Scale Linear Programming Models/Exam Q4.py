import numpy as np
import scipy.sparse as sp
import cplex as cp
import matplotlib.pyplot as plot

def knapsack_problem(weights_file, values_file, capacity_file):
    
    weights = np.loadtxt(weights_file)
    values = np.loadtxt(values_file)
    capacity = np.loadtxt(capacity_file)
    
    N = weights.size
    C = capacity
    
    c = values
    l = np.repeat(0, N)
    u = np.repeat(1, N)
    senses = np.repeat("L")
    types = np.repeat("B", N)
    aij = weights
    row = np.repeat(0, N)
    col = np.repeat(range(N), 1)
    A = sp.csr_matrix(aij, (row, col), shape=(1, N))
    b = np.array([C])
    
    pass
    