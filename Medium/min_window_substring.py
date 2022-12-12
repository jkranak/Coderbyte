# Have the function MinWindowSubstring(strArr) take the array of strings stored in strArr, which will contain only two strings, the first
# parameter being the string N and the second parameter being a string K of some characters, and your goal is to determine the smallest substring
# of N that contains all the characters in K. For example: if strArr is ["aaabaaddae", "aed"] then the smallest substring of N  that 
# contains the characters a, e, and d is "dae" located at the end of the string. So for this example your program should return the string dae.

# Another example: if strArr is ["aabdccdbcacd", "aad"] then the smallest substring of N that contains all of the characters in K is 
# "aabd" which is located at the beginning of the string. Both parameters will be strings ranging in length from 1 to 50 characters and 
# all of K's characters will exist somewhere in the string N. Both strings will only contains lowercase alphabetic characters.

def MinWindowSubstring(strArr):
  right_obj = {}
  right_count = len(strArr[1])

  # We create a count of all the characters in the right string
  for char in strArr[1]:
    if char in right_obj:
      right_obj[char] += 1
    else:
      right_obj[char] = 1
  
  # This function checks that all the characters in the right string are in the given substring
  def is_valid(string):
    str_obj = {}
    counter = 0
    for char in string:
      if char in right_obj:
        counter += 1
        if char in str_obj:
          str_obj[char] += 1
        else:
          str_obj[char] = 1
    if counter >= right_count:
      for key in right_obj:
        if not key in str_obj or str_obj[key] < right_obj[key]:
          return False
      return True
    else:
      return False

  # We loop by length and index. The smallest length will be the length of the right string
  for l in range(right_count, len(strArr[0]) + 1):
    for s in range(0, len(strArr[0]) - l + 1):
      if strArr[0][s] in right_obj and strArr[0][s+l - 1] in right_obj:
        temp_str = strArr[0][s:s+l]
        if is_valid(temp_str):
          return temp_str
