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

def transportation_problem(costs_file, capacities_file, flows_file):
    costs = np.loadtxt(costs_file)
    capacities = np.loadtxt(capacities_file)
    flows = np.loadtxt(flows_file)

    NODES = capacities.shape[0]
    PRODUCTS = costs.shape[0] // capacities.shape[0]
    PATHS = flows.shape[0] // PRODUCTS

    c = costs[:, 3]
    senses = np.concatenate((np.repeat("E", PATHS * PRODUCTS), np.repeat("L", NODES)))
    # First E's are for demand supply relation, the other one is for capacity of each path
    b = np.concatenate((flows[:, 2], capacities[:, 2]))
    l = np.repeat(0, NODES * PRODUCTS)
    u = np.repeat(cp.infinity, NODES * PRODUCTS)
    # lower and upper bounds are pretty appearent

    aij = np.concatenate((np.repeat([+1.0, -1.0], NODES * PRODUCTS), np.repeat(+1.0, NODES * PRODUCTS)))
    # first part is for demand supply relation, second one is for path capacity relation
    row = np.concatenate((
        (costs[:, 0].astype(int) - 1 + (costs[:, 2].astype(int) - 1) * PATHS), 
        (costs[:, 1].astype(int) - 1 + (costs[:, 2].astype(int) - 1) * PATHS),
        (PATHS * PRODUCTS + np.repeat(range(NODES), PRODUCTS))))
    col = np.concatenate((range(NODES * PRODUCTS), range(NODES * PRODUCTS), np.array(range(NODES * PRODUCTS)).reshape(PRODUCTS, NODES).T.flatten()))
    A = sp.csr_matrix((aij, (row, col)), shape = (PATHS * PRODUCTS + NODES, NODES * PRODUCTS))

    import matplotlib.pyplot as plt
    plt.figure(figsize = (6.4, 7.0))
    plt.spy(A, marker = "o", markersize = 6)
    plt.show()
    
    return linear_programming("minimize", A,senses, b, c, l, u)

print(np.array([3,5])*2)