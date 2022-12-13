# Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. 
# Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). 
# Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.

def LetterChanges(strParam):
  output = ''
  vowels = 'dhnt'
  for char in strParam:
    if char == 'z':
      output += 'A'
    elif char in vowels:
      output += chr(ord(char) + 1).upper()
    elif char.isalpha():
      output += chr(ord(char) + 1)
    else:
      output += char
  return output
