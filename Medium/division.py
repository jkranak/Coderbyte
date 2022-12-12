# Have the function Division(num1,num2) take both parameters being passed and return the Greatest Common Factor. 
# The range for both parameters will be from 1 to 10^3.

import math
def Division(num1,num2):
  # Factors come in pairs, one greater than and one less than the square root, except in the case of perfect squares
  # That means, we can just loop through all numbers less than the square root, with both divisor and quotient being factors if the quotient is a whole number
  def get_factors(number):
    start = math.floor(math.sqrt(number))
    factors = []
    # We need to go down to 1, so that we include both 1 and the number itself as factors
    for i in range(start, 0, -1):
      if number % i == 0:
        # I add the factors to the list in this way so that they they will be pre-sorted. 
        # The else condition is for perfect squares, since otherwise square roots would be duplicated. For example, 25 would produce [1,5,5,25] but we want [1,5,25]
        factors = [i] + factors + [int(number / i)] if i != int(number / i) else [i]
    return factors
  
  factors1 = get_factors(num1)
  factors2 = get_factors(num2)
  i1 = len(factors1) - 1
  i2 = len(factors2) - 1
  while i1 > 0 and i2> 0:
    # Since the factors are pre-sorted and we want the largest common factor, we start at the end of the list
    if factors1[i1] == factors2[i2]:
      return factors1[i1]
    elif factors1[i1] > factors2[i2]:
      i1 -= 1
    else:
      i2 -= 1
  
  return 1
