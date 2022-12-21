# Have the function StringReduction(str) take the str parameter being passed and return the smallest number you can get through the 
# following reduction method. The method is: Only the letters a, b, and c will be given in str and you must take two different adjacent 
# characters and replace it with the third. For example "ac" can be replaced with "b" but "aa" cannot be replaced with anything. This 
# method is done repeatedly until the string cannot be further reduced, and the length of the resulting string is to be outputted.
 
# For example: if str is "cab", then "ca" can be reduced to "b" and you get "bb" (you can also reduce it to "cc"). The reduction is 
# done so the output should be 2. If str is "bcab", "bc" reduces to "a", so you have "aab", then "ab" reduces to "c", and the final 
# string "ac" is reduced to "b" so the output should be 1.

from collections import Counter
def StringReduction(strParam):
  # If all the letters are the same, it can't be reduced, so return length of the string
  counts = Counter(strParam)
  if len(counts) == 1:
    return len(strParam)
  # We count how many times each letter appears. If all the counts are odd or all are even,
  # it can only be reduced to two letters. Otherwise, it can always be reduced to one letter.
  odd_evens = sum(map(lambda a: a % 2, counts.values()))
  return 2 if odd_evens == 3 or odd_evens == 0 else 1
