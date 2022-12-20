# Have the function SwapII(str) take the str parameter and swap the case of each character. Then, if a letter is between two numbers (without
# separation), switch the places of the two numbers. For example: if str is "6Hello4 -8World, 7 yes3" the output should be 4hELLO6 -8wORLD, 7 YES3.

import re
def SwapII(strParam):
  # We first split the string up into individual words
  word_list = strParam.swapcase().split(' ')
  output_list = []
  for word in word_list:
    # This is what we use to find numbers with letters in between
    word_re = re.search(r'\d[a-zA-Z]+\d', word)
    # If we find any two numbers with letters in between, then we swap the numbers and replace that part of the string
    if word_re:
      string = word_re.group()
      word = word.replace(string, string[-1] + string[1:-1] + string[0])
    output_list.append(word)

  return ' '.join(output_list)
