# # # def print_operation(num1, num2, operation, ret=False):
# # #   """
# # #   num1: first input number as a string
# # #   num2: second input number as a string
# # #   operation: an arithmetic operation as a string
# # #              one of +, -, *, or /
  
# # #   applies the operation to num1 and num2 and
# # #   returns the result as a String if ret is True, 
# # #   prints it otherwise
# # #   """
# # #   ##################################
# # #   ### START OF YOUR CODE: Part 1 ###
# # #   ##################################
  
# # #   a, b = float(num1), float(num2)
# # #   res = 0
# # #   if operation == "+":
# # #     res = a + b
# # #   elif operation == "-":
# # #     res = a - b
# # #   elif operation == "*":
# # #     res = a * b
# # #   elif operation == "/":
# # #     res = a / b

# # #   if ret:
# # #     return str(res)
# # #   else:
# # #     print(str(int(a)) + " " + operation + " " + str(int(b)) + " = " + str(int(res))) 

# # #   ##################################
# # #   ### END OF YOUR CODE: Part 1 #####
# # #   ##################################


# # # ##################################
# # # ### START OF YOUR CODE: Part 2 ###
# # # ##################################
# # # def print_chain_operation_iterative(chain):
# # #   """
# # #   chain: a list representing a sequence of numbers and operations as a string
# # #   [num, num, operation, num, operation, num, operation, ..., num, operation].

# # #   iterates over the chain and applies operations to numbers, 
# # #   computes the total and prints the expression with the total.
# # #   using print_operation() function
# # #   """
# # # ##################################
# # # ### END OF YOUR CODE: Part 2 #####
# # # ##################################
# # # pass


# # # ##################################
# # # ### START OF YOUR CODE: Bonus ####
# # # ##################################
# # # # Uncomment it for solving the Bonus
# # # # def print_chain_operation_recursive(...):


# # # ##################################
# # # ### END OF YOUR CODE: Bonus ######
# # # ##################################    


# # # def input_matrix():
# # #     print("Enter four floating point numbers:")
# # #     ## This function will keep asking for input
# # #     ## numbers from the user until the user enters 4 valid
# # #     ## floating point numbers, and will return the matrix
# # #     ## in row order form 
# # #     ## For example if the user enters the following inputs:
# # #     ## 1.5
# # #     ## 2.0
# # #     ## hi
# # #     ## hello
# # #     ## -3
# # #     ## 4
# # #     ##
# # #     ## Then the function should return (1.5, 2.0, -3.0, 4.0)
# # #     ##########################
# # #     ### START OF YOUR CODE ###
# # #     ##########################
# # #     inputs = []
# # #     for i in ['a','b','c','d']:
# # #       is_valid = False
# # #       while not is_valid:
# # #         x = input(f'enter number {i}:')
# # #         try:
# # #           x = float(x)
# # #           is_valid = True
# # #           inputs.append(x)
# # #         except ValueError:
# # #           print(f'Please enter valid number for {i}')
        

# # #     return (*inputs)
# # #     ##########################
# # #     ###  END OF YOUR CODE  ###
# # #     ##########################
# # #     pass

# # # def inverse(M):        
# # #     ## This function will take a matrix in row order form
# # #     ## if the determinant is 0, it will raise and Exception
# # #     ## otherwise it will return the inverse of the Matrix
# # #     ## in row order form
# # #     ## For example inverse((1,1,1,1)) will result in an
# # #     ## Exception with the following error message:
# # #     ## determinant is 0, inverse does not exist"
# # #     ## and inverse((1,2,3,4)) will return (-2.0, 1.0, 1.5, -0.5)
# # #     ##  THAT YOU MUST NOT USE ANY "if" STATEMENTS IN 
# # #     ## THIS FUNCTION.
# # #     ##########################
# # #     ### START OF YOUR CODE ###
# # #     ##########################



# # #     ##########################
# # #     ###  END OF YOUR CODE  ###
# # #     ##########################
# # #     pass

# # # def matmul(M1, M2):
# # #     ## This function will take M1 and M2 in row order form
# # #     ## and will return M1 multiplied by M2 in row order
# # #     ## for example matmul((1,2,3,4), (2,3,4,5)) will return
# # #     ## (10, 13, 22, 29)
# # #     ##########################
# # #     ### START OF YOUR CODE ###
# # #     ##########################



# # #     ##########################
# # #     ###  END OF YOUR CODE  ###
# # #     ##########################
# # #     pass

# # # def almost_identity(M, epsilon):
# # #     ## This function will take matrix M in row order form and a
# # #     ## small positive number epsilon.
# # #     ## if the absolute difference between any element of
# # #     ## matrix M and the corresponding element of the identiy
# # #     ## matrix is greater than epsilon, you must use assert
# # #     ## statements to show an error message saying:
# # #     ## "This matrix is not equal to the identiy matrix."
# # #     ## Otherwise simply print the following message:
# # #     ## "This matrix is approximately equal to the identiy matrix."
# # #     ## for example almost_identiy((1.1, 0, 0, 0.9), 0.01)
# # #     ## should show the following error:
# # #     ## AssertionError: There is a problem in the inverse function
# # #     ## and almost_identity((1.1, 0, 0, 0.9), 0.2) should
# # #     ## show the following message:
# # #     ## "This matrix is approximately equal to the identiy matrix."
# # #     ## NOTE THAT YOU MUST NOT USE ANY "if" STATEMENTS IN 
# # #     ## THIS FUNCTION.
# # #     ##########################
# # #     ### START OF YOUR CODE ###
# # #     ##########################



# # #     ##########################
# # #     ###  END OF YOUR CODE  ###
# # #     ##########################    
# # #     pass


# # # if __name__ == "__main__":
# # #   # test your solutions for each part here

# # #   ## Airthmetic Operations ##
# # #   # Part 1
# # #   print_operation("5", "2", "+")  # should print "5 + 2 = 7"
# # #   print_operation("3", "4", "-")  # should print "3 - 4 = -1"
# # #   print_operation("4", "2", "*")  # should print "4 * 2 = 8"
# # #   print_operation("6", "3", "/")  # should print "6 / 3 = 2"
# # #   print_operation("1a", "2", "+") # should throw "Cannot convert to a number."
# # #   print_operation("1", "bc", "*") # should throw "Cannot convert to a number."
# # #   print_operation("4", "0", "/")  # should throw "Cannot divide by zero."
# # #   print_operation("4", "0", "%")  # should assert "Unknown operation."

# # #   print("\n====================================\n")

# # #   # Part 2
# # #   print_chain_operation_iterative(["5","2","+","3","+","2","*"]) # should print "5 + 2 + 3 * 2 = 20.0"
# # #   print_chain_operation_iterative(["5","2","/","3","*","2.5","+"]) # should print "5 / 2 * 3 + 2.5 = 10.0"
# # #   print_chain_operation_iterative(["2","6","-","-1","*","4","*"]) # should print "2 - 6 * -1 * 4 = 16.0"
# # #   print_chain_operation_iterative(["3","3","*","1","+","2","/","3","*","5","+"]) # should print "3 * 3 + 1 / 2 * 3 + 5 = 20.0"
# # #   print_chain_operation_iterative(["7","-10","-","17","-","13","-","-1","*","-13","/"]) # should print "7 - -10 - 17 - 13 * -1 / -13 = -1.0"
# # #   print_chain_operation_iterative(["-3","-10","-","3","+","10","*","4","/","3.5","*"]) # should print "-3 - -10 + 3 * 10 / 4 * 3.5 = 87.5"

# # #   print("\n====================================\n")

# # #   # Bonus
# # #   # Uncomment for testing the Bonus
# # #   # print_chain_operation_recursive(["5","2","+","3","+","2","*"]) # should print "5 + 2 + 3 * 2 = 20.0"
# # #   # print_chain_operation_recursive(["5","2","/","3","*","2.5","+"]) # should print "5 / 2 * 3 + 2.5 = 10.0"
# # #   # print_chain_operation_recursive(["2","6","-","-1","*","4","*"]) # should print "2 - 6 * -1 * 4 = 16.0"
# # #   # print_chain_operation_recursive(["3","3","*","1","+","2","/","3","*","5","+"]) # should print "3 * 3 + 1 / 2 * 3 + 5 = 20.0"
# # #   # print_chain_operation_recursive(["7","-10","-","17","-","13","-","-1","*","-13","/"]) # should print "7 - -10 - 17 - 13 * -1 / -13 = -1.0"
# # #   # print_chain_operation_recursive(["-3","-10","-","3","+","10","*","4","/","3.5","*"]) # should print "-3 - -10 + 3 * 10 / 4 * 3.5 = 87.5"

# # #   print("\n====================================\n"

# # #   ## Matrix Operations ##

# # #   # test input_matrix()
# # #   M = input_matrix()
# # #   print("Matrix M in row order form:")
# # #   print(M)
# # #   print(type())

# # #   # M_inv = inverse(M)
# # #   # print("Inverse of matrix M in row order form")
# # #   # print(M_inv)
# # #   # identity = matmul(M, M_inv)
# # #   # print("Result of multiplying M with its inverse in row order form:")
# # #   # print(identity)
# # #   # almost_identity(identity, 1e-4)

# # # def possible_path_generator(number_of_attempts, list_of_paths=[[]]):
# # #     if number_of_attempts == 0:
# # #       return list_of_paths
# # #     else:
# # #       new_list_of_paths = []
# # #       for index, item in enumerate(list_of_paths):
# # #         new_list_of_paths.append(item + ["R"])
# # #         new_list_of_paths.append(item + ["L"])
# # #       return possible_path_generator(number_of_attempts - 1 , new_list_of_paths)
# # # box_list = [3,2,1,6,7,13]
# # # def path_sum(current_path:list, current_box_list = box_list, sum = 0):
# # #     if len(current_path) == 1:
# # #       if current_path[0] == "R":
# # #         sum += current_box_list[-1]
# # #       elif current_path[0] == "L":
# # #         sum += current_box_list[0]
# # #       return sum
# # #     else:
# # #       if current_path[0] == "R":
# # #         sum += current_box_list[-1]
# # #         return path_sum(current_path[1:], box_list[0:-1],sum)
# # #       elif current_path[0] == "L":
# # #         sum += current_box_list[0]
# # #         return path_sum(current_path[1:], box_list[1:],sum)
# # # def dict_maker(remaining_paths:list, dict_to_return:dict = {}):
# # #     if len(remaining_paths) == 1:
# # #       dict_to_return[tuple(remaining_paths[0])] = path_sum(remaining_paths[0])
# # #       return dict_to_return
# # #     else:
# # #       dict_to_return[tuple(remaining_paths[0])] = path_sum(remaining_paths[0])
# # #       return dict_maker(remaining_paths[1:])
# # # print(max(dict_maker(possible_path_generator(3)).keys())


# # # def find_paths
# # # M = 2 # input ex: 2
# # # N = 3 # input ex: 3

# # # # get grid elements and convert to flat list
# # # grid = [[1,4,3],
# # #         [5,6,7]] # input ex: 1 4 3 5 6 7

# # # # convert flat list to matrix
# # # print(grid)

# # def single_sequence_maker(words_to_continue, selected_word_list:list, current_chain =[]):
# #     new_words_to_continue = []
# #     new_selected_word_list = selected_word_list[:]
# #     if type(words_to_continue) is str:
# #       words_to_continue = [words_to_continue]
# #     if current_chain == []:
# #       current_chain = words_to_continue
# #     word_found = False
# #     for word in words_to_continue:
# #       new_current_chain = []
# #       for word_to_check in selected_word_list:
# #         if word[-1] == word_to_check[0]:
# #           word_found = True
# #           new_current_chain.append(current_chain + [word_to_check])
# #           new_words_to_continue.append(word_to_check)
# #           new_selected_word_list.remove(word_to_check)
# #       if not word_found:
# #               return current_chain
# #       else:
# #               return single_sequence_maker(new_words_to_continue, new_selected_word_list, new_current_chain)
    
# # print(single_sequence_maker("trace", ['angel', 'earth', 'empty', 'level', 'light', 'thank', 'theme']))
# import copy

# def convert_to_dict(selected_word_list):
#   # your code here
#   output_dict = {}
#   for word in selected_word_list:
#     output_dict[word[0]] = output_dict.get(word[0],[]) + [word]
#   return output_dict

# def longest_sequence_fast(beginning_word, selected_word_dict:dict):
#   # your code here
#   def sequence_creator(current_sequences):
#     new_outer_sequence = []
#     continue_bool = False
#     for list1 in current_sequences:
#       new_inner_sequence = []
#       reference_selected_word_dict = copy.deepcopy(selected_word_dict)
#       for word1 in list1:
#           if word1 in reference_selected_word_dict[word1[0]]:
#             reference_selected_word_dict[word1[0]].remove(word1)
#       words_to_add = reference_selected_word_dict.get(word1[-1], [])
#       if words_to_add == []:
#         continue
#       for word2 in words_to_add:
#         continue_bool = True
#         new_inner_sequence.append(list1 + [word2]) 
#       new_outer_sequence.extend(new_inner_sequence)
#     if not continue_bool:
#       return current_sequences
#     else:
#       return sequence_creator(new_outer_sequence)
    

#   all_sequences = sequence_creator([[beginning_word]])
#   longest_sequence = max(all_sequences, key = len)
#   return len(longest_sequence), longest_sequence
class coordinates:
  def __init__(self1,self2):
    x = self1
    y = self2
  def add(self, coordinate_to_add):
    self.x = self.x + coordinate_to_add.x
    self.y = self.y + coordinate_to_add.y

my_cord = coordinates((15,10))
print(my_cord)
my_cord.add((14,20))
print(my_cord)
