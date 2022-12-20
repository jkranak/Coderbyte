# Have the function FibonacciChecker(num) return the string yes if the number given is part of the Fibonacci sequence.   
# This sequence is defined by: Fn = Fn-1 + Fn-2, which means to find Fn you add the previous two numbers up. The first 
# two numbers are 0 and 1, then comes 1, 2, 3, 5 etc. If num is not in the Fibonacci sequence, return the string no.

def FibonacciChecker(num):
  fib1 = 0
  fib2 = 1
  while fib2 < num:
    temp_fib = fib2
    fib2 += fib1
    fib1 = temp_fib
  return 'yes' if fib2 == num else 'no'
