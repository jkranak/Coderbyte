# Have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an acceptable sequence by either 
# returning the string true or false. The str parameter will be composed of + and = symbols with several characters between them 
# (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol. So the string to the left would 
# be false. The string will not be empty and will have at least one letter.

def SimpleSymbols(strParam):
  for i in range(0, len(strParam)):
    if (strParam[i].isalpha() and
    (i == 0 or i == len(strParam) - 1 or strParam[i - 1] != '+' or strParam[i + 1] != '+')):
      return 'false'
  return 'true'
