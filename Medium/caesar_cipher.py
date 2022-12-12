# Have the function CaesarCipher(str,num) take the str parameter and perform a Caesar Cipher shift on it using  
# the num parameter as the shifting number. A Caesar Cipher works by shifting each letter in the string N places 
# in the alphabet (in this case N will be num). Punctuation, spaces, and capitalization should remain intact.

from string import ascii_lowercase as lc, ascii_uppercase as uc
def CaesarCipher(strParam,num):
  # We first create an object, with the key being the plaintext and the value being the cyphertext
  letters = {**dict(zip(lc, lc[num:] + lc[:num])), **dict(zip(uc, uc[num:] + uc[:num]))}
  # We loop through the characters in strParam. If it's a letter, we encode it with the letters object, otherwise, it's unchanged.
  return ''.join(map(lambda a: letters[a] if a in letters else a, strParam))
