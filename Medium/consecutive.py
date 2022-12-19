# Have the function Consecutive(arr) take the array of integers stored in arr and return the minimum number of integers needed to make the contents of arr consecutive 
# from the lowest number to the highest number. For example: If arr contains [4, 8, 6] then the output should be 2 because two numbers need to be added to the
# array (5 and 7) to make it a consecutive array of numbers from 4 to 8. Negative numbers may be entered as parameters and no array will have less than 2 elements.

def Consecutive(arr):
  # The number of consecutive elements is equal to the difference between the largest number and smallest, plus 1. 
  # So, we just need to caluculate the difference between the this number and the length of the list.
  return max(arr) - min(arr) - len(arr) + 1
