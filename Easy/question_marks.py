# Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, 
# and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. 
# If so, then your program should return the string true, otherwise it should return the string false. 
# If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

import re
def QuestionsMarks(strParam):
  # This filters out everything in the string that's not a number of question mark
  str_filtered = ''.join(re.findall('[\d\?]', strParam))
  add_up_to_ten = False
  # if after being filtered, lenth is less than 5, then there can't be an cases of numbers adding up to 10 with 3 question marks between them
  if len(str_filtered) < 5:
    return False
  for i in range(0, len(str_filtered) - 1):
    # The for loop skips over question marks, since we're looking for sections with questions marks between two numbers
    if not str_filtered[i].isnumeric():
      continue
    first_match = re.match('\d\?*\d', str_filtered[i:])
    # Once we find question marks between two numbers, if the numbers add up to 10 and don't have three question marks, we return false
    if first_match and int(first_match.group()[0]) + int(first_match.group()[-1]) == 10:
      # This variable tracks whether we've found any set of numbers adding up to 10 with three queestion marks in between
      add_up_to_ten = True
      # Since we've filtered out everything but numbers and question marks and we're looking for two single numbers with question marks in between, 
      # if length is not five, we know there aren't three question marks in between
      if len(first_match.group()) != 5:
        return False
  # Will only return true if we found on pair of numbers that add up to ten with 3 question marks in between
  return add_up_to_ten
