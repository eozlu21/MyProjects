def find_paths(m, n, all_paths, func_matrix:list, current_path:list = [], row:int = 0, column:int = 0):
  # your code here
  new_all_paths = []
  current_element = func_matrix[row][column]
  new_right_path = None
  new_left_path = None
  new_upper_path = None
  new_lower_path = None
  if current_path == []:
    new_right_path = [current_element]
    new_left_path  = [current_element]
    new_upper_path = [current_element]
    new_lower_path = [current_element]
  if column%n != len(func_matrix[0])-1:
    right_element = func_matrix[row][column+1]
  else:
    right_element = None
  if column != 0:
    left_element = func_matrix[row][column-1]
  else:
    left_element = None
  if row != 0:
    upper_element = func_matrix[row-1][column]
  else:
    upper_element = None
  if row%m != len(func_matrix) - 1 :
    lower_element = func_matrix[row+1][column]
  else:
    lower_element = None
  if (right_element is not None) and right_element > current_element:
    if new_right_path is not None:
      new_right_path += current_path + [right_element]
    else:
      new_right_path = current_path + [right_element]
    new_all_paths.append(new_right_path)
  if (left_element is not None) and left_element > current_element:
    if new_left_path is not None:
      new_left_path += current_path + [left_element]
    else:
      new_left_path = current_path + [left_element]
    new_all_paths.append(new_left_path)
  if (upper_element is not None) and upper_element > current_element:
    if new_upper_path is not None:
      new_upper_path += current_path + [upper_element]
    else:
      new_upper_path = current_path + [upper_element]
    new_all_paths.append(new_upper_path)
  if (lower_element is not None) and lower_element > current_element:
    if new_lower_path is not None:
      new_lower_path += current_path + [lower_element]
    else:
      new_lower_path = current_path + [lower_element]
    new_all_paths.append(new_lower_path)
  if new_right_path is not None and new_right_path != [func_matrix[0][0]]:
    find_paths(m,n,all_paths, func_matrix, current_path=new_right_path, row= row, column= column + 1)
  if new_left_path is not None and new_left_path != [func_matrix[0][0]]:
    find_paths(m,n,all_paths, func_matrix, current_path=new_left_path, row= row, column= column -1)
  if new_upper_path is not None and new_upper_path != [func_matrix[0][0]]:
    find_paths(m,n,all_paths, func_matrix, current_path=new_upper_path, row= row-1, column= column)
  if new_lower_path is not None and new_lower_path != [func_matrix[0][0]]:
    find_paths(m,n,all_paths, func_matrix, current_path=new_lower_path, row= row+1, column= column)
  if new_left_path is None and new_right_path is None and new_upper_path is None and new_lower_path is None:
    all_paths.append(current_path)
  

  
  






if __name__ == "__main__":

  M = int(input("Number of rows:")) # input ex: 2
  N = int(input("Number of columns:")) # input ex: 3

  # get grid elements and convert to flat list
  grid = [int(x) for x in input("Grid elements: ").split()] # input ex: 1 4 3 5 6 7

  # convert flat list to matrix
  grid = [grid[i*N:i*N+N] for i in range(M)] 
  
  all_paths = []
  find_paths(M,N,all_paths,grid) # pass your arguments in ...
  print(all_paths) 
