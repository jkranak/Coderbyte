# Have the function VowelCount(str) take the str string parameter being passed and return the number of vowels the 
# string contains (ie. "All cows eat grass and moo" would return 8). Do not count y as a vowel for this challenge.

import re
def VowelCount(strParam):
  return len(re.findall('[aeiou]', strParam))
