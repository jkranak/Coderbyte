# Have the function PrimeChecker(num) take num and return 1 if any arrangement of num comes out to be a prime number, otherwise return
# 0. For example: if num is 910, the output should be 1 because 910 can be arranged into 109 or 019, both of which are primes.

from math import sqrt, floor
from itertools import permutations

def PrimeChecker(num):
  
  # To check if something is prime we only need to check numbers less than the square root,
  # since factors always come in pairs, one above and one below the square root, except with
  # perfect squares, where the square root is a whole number
  def is_prime(n):
    if n <= 1:
      return False
    start = floor(sqrt(n))
    for i in range(start, 1, -1):
      if n % i == 0:
        return False
    return True

  for c in permutations(list(str(num))):
    if is_prime(int(''.join(c))):
      return 1
  return 0
