# The code for merge sort from lecture slides
def merge(left, right):
  result = []
  i, j = 0, 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  while i < len(left):
    result.append(left[i])
    i += 1
  while j < len(right):
    result.append(right[j])
    j += 1

  return result

def merge_sort(L):
  if len(L) < 2:
    return L[:]
  else:
    middle = len(L) // 2
    left = merge_sort(L[:middle])
    right = merge_sort(L[middle:])
    return merge(left, right)

##########################
### START OF YOUR CODE ###
##########################
# Type your answer for complexity as a comment
# at the beginning of each function

def compare_nested(...):
  # Complexity: 

def compare_sorted(...):
  # Complexity: 

def compare_clever(...):
  # Complexity: 

##########################
###  END OF YOUR CODE  ###
##########################

if __name__ == "__main__":
  # test your solution here

  v1 = [5,3,2,1,4]
  v2 = [4,2,3,1,5]
  v3 = [3,4,5,1,2]
  v4 = [2,5,1,4,3]
  v5 = [4,2,3,1,6]

  print(compare_nested(v1, v2)) # => True
  print(compare_nested(v3, v4)) # => True
  print(compare_nested(v1, v5)) # => False

  print(compare_sorted(v1, v2)) # => True
  print(compare_sorted(v3, v4)) # => True
  print(compare_sorted(v1, v5)) # => False

  print(compare_clever(v1, v2)) # => True
  print(compare_clever(v3, v4)) # => True
  print(compare_clever(v1, v5)) # => False