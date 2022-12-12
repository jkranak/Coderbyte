# Have the function ArithGeoII(arr) take the array of numbers stored in arr and return the string "Arithmetic" 
# if the sequence follows an arithmetic pattern or return "Geometric" if it follows a geometric pattern. If 
# the sequence doesn't follow either pattern return -1. An arithmetic sequence is one where the difference 
# between each of the numbers is consistent, where as in a geometric sequence, each term after the first is 
# multiplied by some constant or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54].
# Negative numbers may be entered as parameters, 0 will not be entered, and no array will contain all the same elements.

def ArithGeoII(arr):
  is_arith = True
  a_diff = arr[1] - arr[0]
  # If arr[1]/arr[0] is not a whole number, then we know it can't be geometric, so we set ratio to 0
  g_ratio = arr[1] / arr[0] if arr[1] % arr[0] == 0 else 0
  for i in range(1, len(arr) - 1):
    if is_arith and arr[i + 1] - arr[i] == a_diff:
      g_ratio = 0
    elif g_ratio > 0 and arr[i + 1] / arr[i] == g_ratio:
      is_arith = False
    else:
      return -1
  return 'Arithmetic' if is_arith else 'Geometric'
