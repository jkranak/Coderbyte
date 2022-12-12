# Have the function PalindromeTwo(str) take the str parameter being passed and return the string true if the  
# parameter is a palindrome, (the string is the same forward as it is backward) otherwise return the string false. 
# The parameter entered may have punctuation and symbols but they should not affect whether the string is in fact 
# a palindrome. For example: "Anne, I vote more cars race Rome-to-Vienna" should return true.

import math
def PalindromeTwo(strParam):
  # We first filter out everything except letters, and make all letters lowercase
  letters = [a for a in strParam.lower() if a.isalpha()]
  halfway = math.floor(len(letters)/2)
  j = len(letters) - 1
  # To check if it's a palindrome, I use two pointers, one starting at the end and one at the beginning, which move towards the middle
  for i in range(0, halfway):
    if letters[j] != letters[i]:
      return False
    j -= 1
  return True
