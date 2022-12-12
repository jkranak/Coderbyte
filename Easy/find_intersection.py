# Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: 
# the first element will represent a list of comma-separated numbers sorted in ascending order, 
# the second element will represent a second list of comma-separated numbers (also sorted). 
# Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. 
# If there is no intersection, return the string false.

def FindIntersection(strArr):
  list1 = strArr[0].split(', ')
  list2 = strArr[1].split(', ')
  result = []
  # This is just a way of stopping the loop when the length of either equals 0
  while len(list1) * len(list2) > 0:
    # We're always looking at the first item in both lists
    # If there is a maptch, we remove it from both lists and add it to results
    if list1[0] == list2[0]:
      list1.pop(0)
      result.append(list2.pop(0))
     # Since both lists are sorted, then we remove the smaller of the first items in the list
    elif int(list1[0]) > int(list2[0]):
      list2.pop(0)
    elif int(list2[0]) > int(list1[0]):
      list1.pop(0)
  return ','.join(result) if len(result) > 0 else False
