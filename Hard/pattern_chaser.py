# Have the function PatternChaser(str) take str which will be a string and return the longest pattern within the string. 
# A pattern for this challenge will be defined as: if at least 2 or more adjacent characters within the string repeat at 
# least twice. So for example "aabecaa" contains the pattern aa, on the other hand "abbbaac" doesn't contain any pattern. 
# Your program should return yes/no pattern/null. So if str were "aabejiabkfabed" the output should be yes abe. If str were 
# "123224" the output should return no null. The string may either contain all characters (a through z only), integers, or both. 
# But the parameter will always be a string type. The maximum length for the string being passed in will be 20 characters. 
# If a string for example is "aa2bbbaacbbb" the pattern is "bbb" and not "aa". You must always return the longest pattern possible.

def PatternChaser(strParam):
  # We first start by finding all characters that repeat at least twice and counting their repeats, with the doubles object
  counts = {}
  doubles = {}
  for c in strParam:
    if c in counts:
      if c in doubles:
        doubles[c] += 1
      else:
        doubles[c] = 2
    else:
      counts[c] = 1
  # The longest possible pattern is the sum of the number of repeats of each characters divided by two. We start with this length string in our for loop below
  length = sum(map(lambda a: int(a / 2), doubles.values()))
  # If there are no repeats, then we know there can't be any patterns and return 'no null'
  if len(doubles) == 0 or length < 2:
    return 'no null'
  # Our outer for loop is length, and starts with the longest possible pattern and then increments down, stopping at two
  for l in range(length, 1, -1):
    # We use the sub_strs object to track any repeated substring. Key is the substring itself and the value is its index
    sub_strs = {}
    for i in range(len(strParam) - l + 1):
      # If any substring repeats we return it. We also need to check that the two matching substrings don't overlap. So they must be seperated by at least l length
      if strParam[i:i+l] in sub_strs and i - sub_strs[strParam[i:i+l]] >= l:
        return f'yes {strParam[i:i+l]}'
      else:
        sub_strs[strParam[i:i+l]] = i
  return 'no null'
