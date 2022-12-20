# Have the function ThreeFiveMultiples(num) return the sum of all the multiples of 3 and 5 that are below num. 
# The integer being passed will be between 1 and 100.

def ThreeFiveMultiples(num):
  output = 0
  for n in range(3, num):
    if n % 3 == 0 or n % 5 == 0:
      output += n
  
  return output
