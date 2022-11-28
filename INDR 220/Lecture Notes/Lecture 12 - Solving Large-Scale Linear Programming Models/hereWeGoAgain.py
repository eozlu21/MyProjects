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

def multiCommodity(ceyda):
    
    capacities = np.loadtxt("capacities{}.txt".format(ceyda))
    costs = np.loadtxt("costs{}.txt".format(ceyda))
    flows = np.loadtxt("flows{}.txt".format(ceyda))
    
    N = max(capacities[:,0:2].astype(int).flatten())
    K = flows.shape[0] // N
    V = costs.shape[0]
    E = V//K
    
    u = np.repeat(cp.infinity, V)
    l = np.repeat(0, V)
    c = costs[:,-1]
    b = np.concatenate((flows[:,-1], capacities[:, -1]))
    senses = np.concatenate((np.repeat("G", flows.shape[0]), np.repeat("L", capacities.shape[0])))
    
    aij = np.concatenate((np.repeat([1,-1], V), np.repeat(1,V)))
    row = np.array([])
    for i in range(K):
        row = np.concatenate((row, (capacities[:,0].astype(int) + i * N) - 1))
    for i in range(K):
        row = np.concatenate((row, (capacities[:,1].astype(int) + i * N) - 1))
    
    row = np.concatenate((row, np.repeat(range(flows.shape[0], flows.shape[0] + E), K)))
    
    col = np.concatenate((range(V), range(V), np.array(range(V)).reshape(K,E).T.flatten()))
    
    A = sp.csr_matrix((aij, (row,col)), shape = (b.shape[0],V))
    
    import matplotlib.pyplot as plt
    plt.figure(figsize = (6.4, 7.0))
    plt.spy(A, marker = "o", markersize = 6)
    plt.show()
    
    (x, obj) = linear_programming("minimize", A, senses, b, c, l, u)
    return (x, obj)