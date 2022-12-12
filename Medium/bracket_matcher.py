# Have the function BracketMatcher(str) take the str parameter being passed and return 1 if the brackets
# are correctly matched and each one is accounted for. Otherwise return 0. For example: if str is "(hello (world))", 
# then the output should be 1, but if str is "((hello (world))" the the output should be 0 because the brackets do
# not correctly match up. Only "(" and ")" will be used as brackets. If str contains no brackets return 1.

def BracketMatcher(strParam):
  left_parens = 0
  right_parens = 0
  for char in strParam:
    if char == '(':
      left_parens += 1
    elif char == ')':
      right_parens += 1
      # if there are ever more close parentheses than open parentheses then this is invalid (it means a close parenthese is before an open parentheses)
    if right_parens > left_parens:
      return 0
    # Also, if the number of close parentheses doesn't equal the number of open parentheses, then it's is invalid too. Otherwise, it's valid.
  return 1 if left_parens == right_parens else 0
