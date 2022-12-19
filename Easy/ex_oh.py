# Have the function ExOh(str) take the str parameter being passed and return the string true if there is an equal number of x's and o's, 
# otherwise return the string false. Only these two letters will be entered in the string, no punctuation or numbers.

def ExOh(strParam):
  return strParam.count('x') == strParam.count('o')
