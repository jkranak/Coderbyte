# Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it.
# For the test cases, the range will be between 1 and 18 and the input will always be an integer.

def FirstFactorial(num):
  output = 1
  for i in range(2, num + 1):
    output *= i
  return output
