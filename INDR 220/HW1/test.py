import numpy as np


def minimum_cost_flow_problem(costs_file, capacities_file, flows_file):
    
    #implement your algorithm here

    # Load in all the matrices
    flows_matrix = np.loadtxt(flows_file)
    costs_matrix = np.loadtxt(costs_file)
    capacities_matrix = np.loadtxt(capacities_file)
    
    capacities_list = sorted(capacities_matrix.tolist())
    costs_list = costs_matrix.tolist()
    flows_list = flows_matrix.tolist()
    

    flows_list.sort()
    costs_list.sort()
    
    # Define the number of nodes
    N = flows_matrix.shape[0]

    # Name all the variables and keep track of the variable count

    var_names = ["x_" + str(int(capacities_list[i][0])) + "_" + str(int(capacities_list[i][1])) for i in range(len(capacities_list))]
    var_name_list = [(int(capacities_list[i][0]), int(capacities_list[i][1])) for i in range(len(capacities_list))]
    print(var_name_list)
    num_of_vars = len(var_names)

    # store the costs, constraints and upper bounds in seperate lists
    c = [costs_list[i][2] for i in range(num_of_vars)]
    b = [flows_list[i][1] for i in range(N)]
    u = [capacities_list[i][2] for i in range(num_of_vars)]

    # create "equal" senses for all constraints
    senseArray = np.repeat("E", N)

    # create the nonzero lower bounds
    lArray = np.repeat(0, num_of_vars)

    # turn these two arrays into lists
    senses = senseArray.tolist()
    l = lArray.tolist()

    # initialize the A matrix
    A = np.zeros((N,num_of_vars))

    # add lhs for the constraints to A
    for var_tuple in var_name_list:

        indice1 = var_tuple[0]
        indice2 = var_tuple[1]
        var_index = var_name_list.index(var_tuple)

        A[indice1 - 1 , var_index] = 1
        A[indice2 - 1 ,  var_index] = -1
        
    problem = cp.Cplex()
    problem.objective.set_sense(problem.objective.sense.minimize)
    problem.variables.add(obj = c, lb = l, ub = u)
    problem.linear_constraints.add(senses = senses, rhs = b)
    row_indices, col_indices = A.nonzero()
    A_sparse = sp.csr_matrix(A)
    problem.linear_constraints.set_coefficients(zip(row_indices.tolist(),
                                                 col_indices.tolist(),
                                                 A_sparse.data.tolist()))
    # solve the problem
    problem.solve()

    # get the solution
    x_star = problem.solution.get_values()
    obj_star = problem.solution.get_objective_value()

    return(x_star, obj_star)

print(minimum_cost_flow_problem("costs.txt", "capacities.txt", "flows.txt"))