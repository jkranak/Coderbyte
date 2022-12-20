# Have the function MultipleBrackets(str) take the str parameter being passed and return 1 #ofBrackets if the
# brackets are correctly matched and each one is accounted for. Otherwise return 0. For example: if str is 
# "(hello [world])(!)", then the output should be 1 3 because all the brackets are matched and there are 3
# pairs of brackets, but if str is "((hello [world])" the the output should be 0 because the brackets do not
# correctly match up. Only "(", ")", "[", and "]" will be used as brackets. If str contains no brackets return 1.

def MultipleBrackets(strParam):
  bracket_count = 0
  # open_stack is a stack of open brakets and parentheses. Our strategy it to check that close brackets match the last bracket on the stack
  open_stack = []
  for b in strParam:
    if b == '(' or b == '[':
      open_stack.append(b)
      bracket_count += 1
      continue
    if b == ']' or b == ')':
    # If there are no open brackets when a close brackets appears, then it's invalid
      if len(open_stack) == 0:
        return 0
      last_open = open_stack.pop(-1)
      if (last_open == '(') == (b == ']'):
        return 0
  if bracket_count == 0:
    return 1
  # If there are still some unclosed open brackets, then it is invalid
  if len(open_stack) > 0:
    return 0

  return f'1 {bracket_count}'
