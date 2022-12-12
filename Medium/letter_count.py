# Have the function LetterCount(str) take the str parameter being passed and return the first word with the greatest number of
# repeated letters. For example: "Today, is the greatest day ever!" should return greatest because it has 2 e's (and 2 t's) and it
# comes before ever which also has 2 e's. If there are no words with repeating letters return -1. Words will be separated by spaces.

def LetterCount(strParam):
  max_word = ''
  max_num = 1
  for word in strParam.split():
    counts = {}
    temp_max_num = 0
    for char in word:
      if char in counts:
        counts[char] += 1
        if counts[char] > temp_max_num:
          temp_max_num = counts[char]
      else:
        counts[char] = 1
    if temp_max_num > max_num:
      max_word = word
      max_num = temp_max_num
  return max_word if max_num > 1 else -1
