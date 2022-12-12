# Have the function StringScramble(str1,str2) take both parameters being passed and return the string true if a portion
# of str1 characters can be rearranged to match str2, otherwise return the string false. For example: if str1 is "rkqodlw"
# and str2 is "world" the output should return true. Punctuation and symbols will not be entered with the parameters.

from collections import Counter
def StringScramble(str1,str2):
  # All we need for this is to count the characters in each string. And as long as every character in str1 is in str2 
  # and in greater than or equal numbers, then it should return true
  count1 = Counter(str1)
  count2 = Counter(str2)
  for key in count2:
    if not key in count1 or count2[key] > count1[key]:
      return False
  return True
