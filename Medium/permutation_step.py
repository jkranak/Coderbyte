# Have the function PermutationStep(num) take the num parameter being passed and return the next number greater than num using the same digits. 
# For example: if num is 123 return 132, if it's 12453 return 12534. If a number has no greater permutations, return -1 (ie. 999).

def PermutationStep(num):
  num_str = str(num)
  # To calculate the next biggest number, we start with the right-most digit and move left. As soon as  
  # we find a digit that's less than the digit to its right, we take all the digits to the left,
  # unchanged, and combine then with that digit and all the digits to the right sorted in descending order.
  # If there is never a digit that is less than the digit to its right, no larger number can be made.
  for i in range(len(num_str) - 1, 0, -1):
    if num_str[i - 1] < num_str[i]:
      slice_l = num_str[:i-1] + num_str[i]
      slice_r = ''.join(list(sorted(num_str[i-1] + num_str[i + 1:])))
      return slice_l + slice_r

  return -1
