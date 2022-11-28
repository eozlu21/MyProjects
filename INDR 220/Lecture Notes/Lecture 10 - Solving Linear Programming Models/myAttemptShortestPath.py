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

def shortest_path_problem(problem_file):
    
    problem = np.loadtxt(problem_file)
    N: int = int(max(problem[:,0:2].flatten()))
    problem = np.vstack((problem, np.array([N,1,0])))
    E: int = problem.shape[0]

    c = problem[:,-1]
    u = np.repeat(cp.infinity, E)
    l = np.repeat(0, E)
    senses = np.repeat("E", N)
    b = np.concatenate((np.array([1]), np.repeat(0, N - 2), np.array([-1])))
    
    aij = np.repeat([1,-1], E)
    row = np.concatenate((problem[:,0].astype(int) - 1, problem[:,1].astype(int) -1))
    col = np.concatenate((range(E), range(E)))
    
    A = sp.csr_matrix((aij, (row, col)), shape=(N,E))
    print(A.toarray())
    
    (x, obj) = linear_programming("minimize", A, senses, b, c, l, u)
    return (x, obj)

print(shortest_path_problem("shortest_path_problem1.txt"))
    
    