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

def coin_distribution_problem(coins_file, M):

    coins = np.loadtxt(coins_file)
    N = coins.shape[0]
    V = M*N

    c = np.repeat(1,V)
    l = np.repeat(0,V)
    u = np.repeat(1,V)
    types = np.repeat("B", V)
    senses = np.repeat("E", M + N)
    coinPerChild = sum(coins) / M
    b = np.concatenate((np.repeat(coinPerChild, M), np.repeat(1,N)))

    aij = np.concatenate((np.repeat(coins, M), np.repeat(1, V)))
    row = np.concatenate((np.tile(range(M), N), np.repeat(range(M, M + N), M)))
    col = np.concatenate((range(V), range(V)))

    A = sp.csr_matrix((aij, (row, col)), shape=(b.shape[0], V))

    X_star, obj_star = mixed_integer_linear_programming("maximize", A, senses, b, c, l, u, types)
    X_star = np.array(X_star).reshape(N,M)
    return (X_star)

print(coin_distribution_problem("coins.txt", 2))