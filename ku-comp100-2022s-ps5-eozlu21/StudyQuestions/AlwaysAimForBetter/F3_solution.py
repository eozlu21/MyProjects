## Part 1

def q1(L, m):
  ##########################
  ### START OF YOUR CODE ###
  ##########################
  pass

  ##########################
  ###  END OF YOUR CODE  ###
  ########################## 

# Test cases
print(q1([8,2,4], 6))
print(q1([8,2,4,12,16,42], 58))
print(q1([8,2,4,12,16,42], 56))

# This should return:
# (True, 6)
# (True, 30)
# (False, 36)


'What is the time complexity of this solution for a list of size N. Please, explain why.'
'ENTER YOUR SOLUTIONS AS A COMMENT.'

############################
### START OF YOUR ANSWER ###
############################
#
#
#
#
#
############################
###  END OF YOUR ANSWER  ###
############################


## Part 2

def binary_search(L, e):
  def binary_search_helper(L, e, low, high, count = 0):
    count += 1
    if high == low:
      return L[low] == e, count
    
    mid = (low + high) // 2
    if L[mid] == e:
      return True, count
    elif L[mid] > e:
      if low == mid: 
        #nothing left to search
        return False, count
      else:
        return binary_search_helper(L, e, low, mid - 1, count)
    else:
      return binary_search_helper(L, e, mid + 1, high, count)
    
  if len(L) == 0:
    return False, 0
  else:
    return binary_search_helper(L, e, 0, len(L) - 1)

def q2(L, m):
  ## assumes list is sorted

  ##########################
  ### START OF YOUR CODE ###
  ##########################
  pass
  

  ##########################
  ###  END OF YOUR CODE  ###
  ########################## 

# Test cases
print(q2(sorted([8,2,4]), 6))
print(q2(sorted([8,2,4,12,16,42]), 58))
print(q2(sorted([8,2,4,12,16,42]), 56))

# This should return:
# (True, 1)
# (True, 15)
# (False, 18)

'What is the time complexity of this solution for a list of size N by excluding the cost of sorting the list? Please, explain why.'
'ENTER YOUR SOLUTIONS AS A COMMENT.'

############################
### START OF YOUR ANSWER ###
############################
#
#
#
#
#
############################
###  END OF YOUR ANSWER  ###
############################


## Part 3

def q3(L, m):
	## assumes list is sorted

  ##########################
  ### START OF YOUR CODE ###
  ##########################
  pass

  ##########################
  ###  END OF YOUR CODE  ###
  ########################## 

# Test cases
print(q3(sorted([8,2,4]), 6))
print(q3(sorted([8,2,4,12,16,42]), 58))
print(q3(sorted([8,2,4,12,16,42]), 56))

# This should return:
# (True, 2)
# (True, 5)
# (False, 5)

'What is the time complexity of this solution for a list of size N by excluding the cost of sorting the list? Please, explain why.'
'ENTER YOUR SOLUTIONS AS A COMMENT.'

############################
### START OF YOUR ANSWER ###
############################
#
#
#
#
#
############################
###  END OF YOUR ANSWER  ###
############################



