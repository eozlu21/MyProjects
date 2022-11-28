import numpy as np
import scipy.sparse as sp
import cplex as cp

def mixed_integer_linear_programming(direction, A, senses, b, c, l, u, types):
    # create an empty optimization problem
    prob = cp.Cplex()

    # add decision variables to the problem including their coefficients in objective and ranges
    prob.variables.add(obj = c.tolist(), lb = l.tolist(), ub = u.tolist(), types = types.tolist())

    # define problem type
    if direction == "maximize":
        prob.objective.set_sense(prob.objective.sense.maximize)
    else:
        prob.objective.set_sense(prob.objective.sense.minimize)

    # add constraints to the problem including their directions and right-hand side values
    prob.linear_constraints.add(senses = senses.tolist(), rhs = b.tolist())

    # add coefficients for each constraint
    row_indices, col_indices = A.nonzero()
    prob.linear_constraints.set_coefficients(zip(row_indices.tolist(), col_indices.tolist(), A.data.tolist()))

    # solve the problem
    print(prob.write_as_string())
    prob.solve()

    # check the solution status
    print(prob.solution.get_status())
    print(prob.solution.status[prob.solution.get_status()])

    # get the solution
    x_star = prob.solution.get_values()
    obj_star = prob.solution.get_objective_value()

    return(x_star, obj_star)

def set_covering_problem(flights_file, costs_file, K):

    flights = np.loadtxt(flights_file)
    costs = np.loadtxt(costs_file)
    flights = flights[flights[:,0].argsort()]
    costs = costs[costs[:,0].argsort()]

    N = max(flights[:, -1].astype(int)) # Route count which is the same as the number of decision variables
    M = max(flights[:, 0].astype(int)) # Leg count
    flightCount = flights.shape[0]

    c = costs[:,-1]
    b = np.concatenate((np.repeat(1,M), np.repeat(K,1)))
    types = np.repeat("B", N)
    senses = np.concatenate((np.repeat("G", M), np.repeat("E", 1)))
    l = np.repeat(0, N)
    u = np.repeat(1, N)

    aij = (np.repeat(1, flightCount + N))
    row = np.concatenate((flights[:,0].astype(int) - 1, np.repeat(M, N)))
    col = np.concatenate((flights[:,1].astype(int) - 1, np.repeat(range(N), 1)))

    A = sp.csr_matrix((aij, (row, col)), shape = (b.shape[0], N))

    # import matplotlib.pyplot as plt
    # plt.figure(figsize = (6, 9))
    # plt.spy(A, marker = "o")
    # plt.show()

    x_star, obj_star = mixed_integer_linear_programming("minimize", A, senses, b, c, l, u, types)
    return (x_star, obj_star)
    
print(set_covering_problem("flights.txt", "costs.txt", 3))