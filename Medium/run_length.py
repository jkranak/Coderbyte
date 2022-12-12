# Have the function RunLength(str) take the str parameter being passed and return a compressed version of the string 
# using the Run-length encoding algorithm. This algorithm works by taking the occurrence of each repeating character 
# and outputting that number along with a single character of the repeating sequence. For example: "wwwggopp" would 
# return 3w2g1o2p. The string will not contain any numbers, punctuation, or symbols.

def RunLength(strParam):
  output_str = ''
  i = 0
  while i < len(strParam):
    count = 1
    for j in range(i + 1, len(strParam)):
      if strParam[j] == strParam[i]:
        count += 1
      else:
        break
    output_str += f'{count}{strParam[i]}'
    i += count
 
  return output_str
