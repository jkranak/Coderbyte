# Have the function TreeConstructor(strArr) take the array of strings stored in strArr, which will 
# contain pairs of integers in the following format: (i1,i2), where i1 represents a child node in a 
# tree and the second integer i2 signifies that it is the parent of i1. Your program should, if a binary
# tree can be formed, return the string true because a valid binary tree can be formed. If a proper binary 
# tree cannot be formed with the integer pairs, then return the string false. All of the integers within 
# the tree will be unique, which means there can only be one node in the tree with the given integer value.

import re
def TreeConstructor(strArr):
  parents = []
  children = []
  # We create a list of all the children and parents
  for string in strArr:
    vals = re.findall(r'\d+', string)
    children.append(vals[0])
    parents.append(vals[1])
  # if a child is the child of two different parents, then a valid binary tree cannot be made
  if len(children) != len(set(children)):
    return False
  par_count = {}
  # Also if a parents has more than two children, then a valid binary tree cannot be made
  for parent in parents:
    if parent in par_count:
      if par_count[parent] > 1:
        return False
      par_count[parent] += 1
    else:
      par_count[parent] = 1
  return True
