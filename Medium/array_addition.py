Have the function ArrayAddition(arr) take the array of numbers stored in arr and return the string true if any combination 
of numbers in the array (excluding the largest number) can be added up to equal the largest number in the array, otherwise 
return the string false. For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return true because  
4 + 6 + 10 + 3 = 23. The array will not be empty, will not contain all the same elements, and may contain negative numbers.

from itertools import combinations
def ArrayAddition(arr):
  max_num = max(arr)
  arr.remove(max_num)
  if max_num in arr:
    return True
  for i in range(len(arr), 1, -1):
    for combo in combinations(arr, i):
      if sum(combo) == max_num:
        return True
  return False
