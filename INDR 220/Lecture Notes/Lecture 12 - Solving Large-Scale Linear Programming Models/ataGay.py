import numpy as np
import scipy.sparse as sp
import cplex as cp

def linear_programming(direction, A, senses, b, c, l, u):
    # create an empty optimization problem
    prob = cp.Cplex()

    # add decision variables to the problem including their coefficients in objective and ranges
    prob.variables.add(obj = c.tolist(), lb = l.tolist(), ub = u.tolist())

    # define problem type
    if direction == "maximize":
        prob.objective.set_sense(prob.objective.sense.maximize)
    else:
        prob.objective.set_sense(prob.objective.sense.minimize)

    # add constraints to the problem including their directions and right-hand side values
    prob.linear_constraints.add(senses = senses.tolist(), rhs = b.tolist())

    # add coefficients for each constraint
    row_indices, col_indices = A.nonzero()
    prob.linear_constraints.set_coefficients(zip(row_indices.tolist(),
                                                 col_indices.tolist(),
                                                 A.data.tolist()))

    # solve the problem
    prob.solve()

    # check the solution status
    print(prob.solution.get_status())
    print(prob.solution.status[prob.solution.get_status()])

    # get the solution
    x_star = prob.solution.get_values()
    obj_star = prob.solution.get_objective_value()

    return(x_star, obj_star)

capacities_file = "capacities2.txt"
costs_file = "costs2.txt"
flows_file = "flows2.txt"

capacities = np.loadtxt(capacities_file)
costs = np.loadtxt(costs_file)
flows = np.loadtxt(flows_file)

c = costs[:,-1]
V = c.shape[0]
E = capacities.shape[0]
K = V//E
N = flows.shape[0] // K

b1 = flows[:,-1]
b2 = capacities[:,-1]
b = np.concatenate((b1, b2))

u = np.repeat(cp.infinity, V)
l = np.repeat(0, V)
senses = np.concatenate((np.repeat("E", N*K), np.repeat("L", E)))

aij = np.concatenate((np.repeat([1,-1], V), np.repeat(1,V)))
row = np.array([])

for i in range(K):
    row = np.concatenate((row, capacities[:,0].astype(int) - 1 + i * N))
for i in range(K):
    row = np.concatenate((row, capacities[:,1].astype(int) - 1 + i * N))
    
row = np.concatenate((row, np.repeat(range(E), K) + K * N))

col = np.concatenate((np.array(range(V)), np.array(range(V)), np.array(range(V)).reshape(V//E, E).T.flatten()))

A = sp.csr_matrix((aij, (row, col)), shape = (b.shape[0], V))

import matplotlib.pyplot as plt
plt.figure(figsize = (6.4, 7.0))
plt.spy(A, marker = "o", markersize = 6)
plt.show()

print(linear_programming("minimize", A, senses, b, c, l ,u))