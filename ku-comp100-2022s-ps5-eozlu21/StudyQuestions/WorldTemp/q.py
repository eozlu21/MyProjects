import glob
import numpy as np

def load_data(load_sorted = False):
  # list all txt files in WorldTemp
  region_paths = glob.glob('WorldTemp/*.txt')

  # load regions
  all_region_temps = []
  for region_path in region_paths:
    # first col: year, second col: temp anomaly
    region = np.loadtxt(region_path)
    
    # take only the temp anomaly
    region_temp = list(region[:,1])

    if load_sorted:
      # sort and append to the big list
      sorted_region_temp = sorted(region_temp)
      all_region_temps.append(sorted_region_temp)
    else:
      all_region_temps.append(region_temp)

  return all_region_temps


# merge sort implementation from the class
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

  while (i < len(left)):
    result.append(left[i])
    i += 1

  while (j < len(right)):
    result.append(right[j])
    j += 1

  # print('merge: ' + str(left) + '&' + str(right) + ' to ' +str(result))
  return result

def merge_sort(L):
  print('merge sort: ' + str(L))

  if len(L) < 2:
    return L[:]
  else:
    middle = len(L)//2
    left = merge_sort(L[:middle])
    right = merge_sort(L[middle:])
    return merge(left, right)


### Part 1 ###

def sort_almost_sorted(region_temp, p = 10):
  '''
  region_temp: a list of anomaly temperature values to be sorted, corresponding to a region's data
  p: the length of the period, a decade by default

  an efficient sort algorithm for a region by assuming that anomalies are sorted across short periods of time p
  '''
  ##########################
  ### START OF YOUR CODE ###
  ##########################
  
  pass # delete this line

  ##########################
  ###  END OF YOUR CODE  ###
  ##########################


# to test your implementation
dummy_region = [4, 3, 6, 8, 5, 10, 1, 9, 7, 2, \
                13, 16, 19, 15, 20, 12, 17, 18, 11, 14, \
                27, 23, 26, 28, 25, 30, 21, 24, 29, 22, \
                42, 47, 44, 50, 45, 48, 41, 46, 43, 49]

assert sorted(dummy_region) == sort_almost_sorted(dummy_region), "sort_almost_sorted: not properly sorted."

######## COMPLEXITY ########

############################
### START OF YOUR ANSWER ###
############################
'''

'''
############################
###  END OF YOUR ANSWER  ###
############################

### Part 2 ###

def combine_regions(region_temps):
  '''
  region_temps: a list of sorted lists where each sorted list corresponds to a region's data

  combines all the region data into a global anomaly data which is also sorted and returns it
  '''
  ##########################
  ### START OF YOUR CODE ###
  ##########################
  
  pass # delete this line

  ##########################
  ###  END OF YOUR CODE  ###
  ##########################


# first load the data sorted
all_region_temps = load_data(load_sorted = True)

# combine sorted region data into global temp
global_temp = combine_regions(all_region_temps)


######## COMPLEXITY ########

############################
### START OF YOUR ANSWER ###
############################
'''
'''
############################
###  END OF YOUR ANSWER  ###
############################