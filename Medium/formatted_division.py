# Have the function FormattedDivision(num1,num2) take both parameters being passed, divide num1 by num2, and return the result 
# as a string with properly formatted commas and 4 significant digits after the decimal place. For example: if num1 is 123456789 
# and num2 is 10000 the output should be "12,345.6789". The output must contain a number in the one's place even if it is a zero.

def FormattedDivision(num1,num2):
  result = num1/num2
  # This is just to get the significant figures. We multiply by 10,000 to make this an integer
  # We add the .5 for rounding, since int() rounds down. We don't use round() since it sometimes rounds 0.5 down.
  sig_figs = '{:0>4}'.format(int((result - int(result)) * 10000 + .5))
  left = '0' if result < 1 else '{:,}'.format(int(result))
  return f'{left}.{sig_figs}'
