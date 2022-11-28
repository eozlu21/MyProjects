def print_halves(input_list):
  """ 
  takes a list input_list as input 
  and returns a new list output_list, the same size
  by halving the value of each element in the input_list
  input_list remains unchaged
  """
  output_list = input_list

  for i in range(len(input_list)):
    output_list[i] //= 2
  
  return output_list


def print_halves_2D(input_list):
  """ 
  takes a 2D list, i.e. list of lists, input_list as input 
  and returns a new 2D list output_list, the same size
  by halving the value of each element in each list in the input_list
  input_list remains unchaged
  """
  output_list = input_list

  for i in range(len(output_list)):
    for j in range(len(output_list[i])):
      output_list[i][j] //= 2
  
  return output_list


def remove_az(l):
  """ 
  takes a list l as input and mutates it
  by removing all occurences of character 'a' and 'z'
  no return, the input is modified directly
  """
  word_to_remove = ["a" , "z"]
  copy_of_l = l[:]
  for i in copy_of_l:
    if i in word_to_remove:
      l.remove(i)


if __name__ == "__main__":
  # test your solutions for each part here

  # Part 1
  input_list = [2, 4, 6, 8, 10]
  output_list = print_halves(input_list)
  print("1) input_list:", input_list)
  print("1) output_list:", output_list)

  print("\n====================================\n")

  # Part 2
  input_list_2D = [[2, 4, 6, 8, 10], [20, 40, 60, 80, 100]]
  output_list_2D = print_halves_2D(input_list_2D)
  print("2) input_list:", input_list_2D)
  print("2) output_list:", output_list_2D)

  print("\n====================================\n")

  # Part 3
  input_list = ["f", "z", "b", "d", "z", "a"]
  print("3) The list before: ", input_list)
  remove_az(input_list)
  print("3) The list after: ", input_list)