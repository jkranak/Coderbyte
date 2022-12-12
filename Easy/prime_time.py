# Have the function PrimeTime(num) take the num parameter being passed and return the string true if the
# parameter is a prime number, otherwise return the string false. The range will be between 1 and 2^16.

import math
def PrimeTime(num):
  # Whoel number factors either come in pairs with one less than and one greater than the square root, or in the case of perfect squares, the factor will be the square root
  # For this reason, we only need to check the numbers on one side of the square root. Since the side less than the square root is smaller, it's better to start at the square root and go down
  start = math.floor(math.sqrt(num))
  for i in range (start, 1, -1):
    if num % i == 0:
      return False
  
  return True
