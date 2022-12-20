# Have the function StringReduction(str) take the str parameter being passed and return the smallest number you can you must take two
# get through the following reduction method. The method is: Only the letters a, b, and c will be given in str and different adjacent 
# characters and replace it with the third. For example "ac" can be replaced with "b" but "aa" cannot be replaced with anything.
# This method is done repeatedly until the string cannot be further reduced, and the length of the resulting string is to be outputted.

# For example: if str is "cab", then "ca" can be reduced to "b" and you get "bb" (you can also reduce it to "cc"). The reduction is 
# done so the output should be 2. If str is "bcab", "bc" reduces to "a", so you have "aab", then "ab" reduces to "c", and the final 
# string "ac" is reduced to "b" so the output should be 1.

import re
def StringReduction(strParam):
  # These are all the replacements of characters
  replacers = {'ab': 'c', 'bc': 'a', 'ac': 'b', 'ba': 'c', 'cb': 'a', 'ca': 'b'}
  # This is a stack for all reductions so far
  str_stack = [strParam]
  # This is a list of completed reductions
  output_list = []
  while len(str_stack) > 0:
    word = str_stack.pop(0)
    matches = False
    for i in range(len(word) - 1):
      ts = word[i] + word[i + 1]
      if ts in replacers:
        matches = True
        tsi = word.index(ts)
        str_stack.append(word[:tsi] + replacers[ts] + word[tsi + 2:])
    if not matches:
      output_list.append(word)
  return min(map(len, output_list))
