
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
  # open_stack is a stack of open brakets and parentheses. Our strategy it to check that close brackets match the last bracket on the stack
  open_stack = []
  for b in all_brackets:
    if b == '(' or b == '[':
      open_stack.append(b)
      continue
    if len(open_stack) == 0:
      return 0
    last_open = open_stack.pop(-1)
    if (last_open == '(') == (b == ']'):
      return 0
  
  return f'1 {int(length / 2)}'
