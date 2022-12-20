
import re
def MultipleBrackets(strParam):
  # We filter out only parentheses and brackets
  all_brackets = ''.join(re.findall(r'\(|\)|\[|\]', strParam))
  length = len(all_brackets)
  if not all_brackets:
    return 1
  # If the number of open brackets parentheses and open brackets doesn't 
  # equal the number of close parentheses and brackets, this is invalid
  if all_brackets.count('(') != all_brackets.count(')') or all_brackets.count('[') != all_brackets.count(']'):
    return 0
  # Our strategy is to continually remove () and []. If we can't ever do it, it's invalid.
  # We can't use the straegy we used in bracket_matcher.py(https://github.com/jkranak/Coderbyte/blob/main/Medium/bracket_matcher.py)
  # because in fails in cases like '[(])', that is in cases of a pair of brackets and parentheses overlapping
  while len(all_brackets) > 0:
    if '()' in all_brackets:
      all_brackets = all_brackets.replace('()', '')
      continue
    if '[]' in all_brackets:
      all_brackets = all_brackets.replace('[]', '')
      continue
    return 0
  
  return f'1 {int(length / 2)}'
