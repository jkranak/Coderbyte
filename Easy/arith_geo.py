# Have the function ArithGeo(arr) take the array of numbers stored in arr and return the string "Arithmetic" if the sequence follows an arithmetic
# pattern or return "Geometric" if it follows a geometric pattern. If the sequence doesn't follow either pattern return -1. An arithmetic sequence is
# one where the difference between each of the numbers is consistent, where as in a geometric sequence, each term after the first is multiplied by  
# some constant or common ratio. Negative numbers may be entered as parameters, 0 will not be entered, and no array will contain all the same elements.

def ArithGeo(arr):
  if len(arr) < 3:
    return -1
  arth_ratio = arr[1] - arr[0]
  if all(arr[i + 1] - arr[i] == arth_ratio for i in range(1, len(arr) - 1)):
    return 'Arithmetic'
  geo_ratio = arr[1] / arr[0]
  if all(arr[i + 1] / arr[i] == geo_ratio for i in range(1, len(arr) - 1)):
    return 'Geometric'
  return -1
