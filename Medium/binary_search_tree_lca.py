# Have the function BinarySearchTreeLCA(strArr) take the array of strings stored in strArr, which will contain 3 elements: 
# the first element will be a binary search tree with all unique values in a preorder traversal array, the second and 
# third elements will be two different values, and your goal is to find the lowest common ancestor of these two values.
# You can assume the two nodes you are searching for in the tree will exist somewhere in the tree.

import re
def BinarySearchTreeLCA(strArr):
  # This extracts all the numbers from strArr[0]
  nodes = list(map(int, re.findall(r'\d+', strArr[0])))
  a = int(strArr[1])
  b = int(strArr[2])
  # If we loop through the nodes, from left to right, the least common ancestor will be the first node that is less than
  # one value and greater than the other. We use <= because it could be that one node itself is an anestor of the other
  for node in nodes:
    if a <= node <= b or b <= node <= a:
      return node
  return -1
