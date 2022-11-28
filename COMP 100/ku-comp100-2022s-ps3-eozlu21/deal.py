
def play_deal(box_list:list, number_of_attempts:int):
  # your code here
  def max_key(dictionary):
      v=list(dictionary.values())
      k=list(dictionary.keys())
      return k[v.index(max(v))]
  
  def possible_path_generator(number_of_attempts, list_of_paths = [[]]):
    """Generates all possible left and right paths according to the number of attempts.
    Takes the number of attempts as input and returns the list of all paths as output."""
    if number_of_attempts == 0:
      return list_of_paths
    else:
      new_list_of_paths = []
      for index, item in enumerate(list_of_paths):
        new_list_of_paths.append(item + ["R"])
        new_list_of_paths.append(item + ["L"])
      return possible_path_generator(number_of_attempts - 1 , new_list_of_paths)


  def path_sum(current_path:list, current_box_list = box_list, sum = 0):
    """Takes a list of R and L string commands as input, returns the sum 
    for that specific route as output."""
    if len(current_path) == 1:
      if current_path[0] == "R":
        sum += current_box_list[-1]
      elif current_path[0] == "L":
        sum += current_box_list[0]
      return sum
    else:
      if current_path[0] == "R":
        sum += current_box_list[-1]
        return path_sum(current_path[1:], current_box_list[0:-1],sum)
      elif current_path[0] == "L":
        sum += current_box_list[0]
        return path_sum(current_path[1:], current_box_list[1:],sum)


  def dict_maker(remaining_paths:list, dict_to_return:dict = {}):
    """Takes the list of all possible routes as input,
    returns a dictionary whose values are the sums of the routes in keys."""
    if len(remaining_paths) == 1:
      dict_to_return[tuple(remaining_paths[0])] = path_sum(remaining_paths[0])
      return dict_to_return
    else:
      dict_to_return[tuple(remaining_paths[0])] = path_sum(remaining_paths[0])
      return dict_maker(remaining_paths[1:])


  all_possible_paths = possible_path_generator(number_of_attempts)
  dict_of_all_path_sums = dict_maker(all_possible_paths)
  return max(dict_of_all_path_sums.values()), max_key(dict_of_all_path_sums)


if __name__ == "__main__":

    num_boxes = int(input("Number of boxes (N): ")) # input ex: 5
    num_attempts = int(input("Number of attempts (K): ")) # input ex: 3
    assert num_boxes >= num_attempts

    boxes = [int(x) for x in input("Boxes: ").split()] # input ex: 1 100 10 20 5
    assert len(boxes) == num_boxes

    max_gain, opt_actions = play_deal(boxes, num_attempts) # pass your arguments in ...
    print("Max gain:", max_gain)
    print("Optimal actions:", " ".join(opt_actions))