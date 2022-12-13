# Have the function SimpleAdding(num) add up all the numbers from 1 to num.

def SimpleAdding(num):
  result = 0
  for i in range(0, num + 1):
    result += i
  return result
