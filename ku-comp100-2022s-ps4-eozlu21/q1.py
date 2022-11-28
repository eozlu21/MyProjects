def q1_a(l, i1, i2):
  """
  Multiplies i1 and i2 indexed elements in list l
  """
  result = l[i1] * l[i2]
  return result


def q1_b():
  """
  Returns amount of apples
  """
  names = ["apples" , "bananas", "grapes"]
  values = [5, 3, 7]

  for idx, name in enumerate(names):
    if name == "apples":
      return values[idx]
    else:
      return None


def q1_c():
  """
  Returns amount of apples
  """

  d = {"apples" : 5, "bananas": 3, "grapes": 7}

  return d["apples"]


def q1_d(l, item):
	"""
	Checks the given item in the given list.
	"""
	for item1 in l:
		if item1 == item:
			return True
	return False


def q1_e(l):
	"""
	Prints all the elements of a list
	"""
	for item in l:
		print(item)


def q1_f(l):
	"""
	Multiplies all the elements in the given list.
	"""
	total = 1
	for item in l:
		total = total * item
	return total


def q1_g(l):

  """
  Finds and returns the maximum value inside a list
  """

  max_value = 0

  for item in l:
    if item > max_value:
      max_value = item

  return max_value


def q1_h(matrix):
  """
  Finds and returns the maximum value inside nested two lists (like a matrix)
  """

  max_value = 0
  for row in matrix:
    for item in row:
      if item > max_value:
        max_value = item

  return max_value


def q1_i(l):
	"""
	Finds the duplicate elements in the given list
	"""
	dups = []

	for i in range(len(l)):
		for j in range(len(l)):
			if i != j and l[i] == l[j]:
				dups.append(l[i])
	return dups


def q1_j(l):
	"""
	Prints all possible pair orderings in the given list.
	"""
	for i in range(len(l)):
		for j in range(len(l)):
			print(l[i],'=',l[j])


def q1_k(tensor):
  """
  Finds and returns the maximum value inside nested three lists (like a matrix)
  """

  max_value = 0

  for matrix in tensor:
    for row in matrix:
      for item in row:
        if item > max_value:
          max_value = item

  return max_value



if __name__ == "__main__":
  print("A: ", q1_a([4,5,6,8],1,2))
  print("B: ", q1_b())
  print("C: ", q1_c())
  print("D: ", q1_d([1,2,3,4,5],3))
  print("E: ", q1_e([4,5,6,7]))
  print("F: ", q1_f([1,2,3,4,5,6]))
  print("G: ", q1_g([2,4,5,6]))
  print("H: ", q1_h([[2,4,5,6],[1,0,0,7]]))
  print("I: ", q1_i([1,2,3,4,1]))
  print("J: ", q1_j([1,2,3,4]))
  print("K: ", q1_k(
    [[[2, 4, 5, 6],
      [1, 0, 9, 7],
      [2, 3, 4, 5]],
      [[5, 4, 5, 8],
      [2, 3, 3, 4],
      [7, 1, 1, 5]]]
  ))
  

