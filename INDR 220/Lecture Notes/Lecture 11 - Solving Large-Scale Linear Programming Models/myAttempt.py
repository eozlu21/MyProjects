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

def product_mix_problem(products_file, resources_file):
    
    products = np.loadtxt(products_file)
    resources = np.loadtxt(resources_file)
    # number of products
    P = products.shape[0]
    # number of resources
    R = resources.shape[0]
    
    # get every single cost value for products, first inside then outside
    c = np.concatenate((products[:,1] , products[:,2]))
    demandArray = np.array(products[:, -1])
    capacityArray = np.array(resources[:, -1])
    b = np.concatenate((demandArray, capacityArray))
    u = np.repeat(cp.infinity, P * 2)
    l = np.repeat(0, P * 2)
    # IMPORTANT: The A matrix is designed so that columns are in the same order as the decision variables
    aij = np.concatenate((np.repeat(1, P*2), resources[:,1:-1].flatten()))
    row = np.concatenate((np.repeat(range(P), 2), np.repeat(range(R), P) + P))
    print(c)
    print(row)
    col = np.concatenate((np.array(range(P*2)).reshape(2,P).T.flatten(), np.tile(range(P), R)))
    M = R + P
    N = 2*P
    senses = np.concatenate((np.repeat("G", P), np.repeat("L", R)))
    A = sp.csr_matrix((aij, (row, col)), shape= (M, N))
    print(A)
    (x_star, obj_star) = linear_programming("minimize", A, senses, b, c, l, u)
    return (x_star, obj_star)


print(product_mix_problem("products3.txt", "resources2.txt"))
    
    
