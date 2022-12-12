# Have the function PrimeMover(num) return the numth prime number. The range will be from 1 to 10^4.

import math
def PrimeMover(num):
  
  def is_prime(number):
    start = math.floor(math.sqrt(number))
    for n in range(start, 1, -1):
      if number % n == 0:
        return False
    return True
  
  counter = 1
  result = 2
  while counter < num:
    result += 1
    if is_prime(result):
      counter += 1
  return result
