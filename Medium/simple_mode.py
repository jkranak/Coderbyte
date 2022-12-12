# Have the function SimpleMode(arr) take the array of numbers stored in arr and return the number that appears most frequently one that For 
# example:if arr contains [10, 4, 5, 2, 4] the output should be 4. If there is more than one mode return the (the mode). appeared in the 
# array first (ie. [5, 10, 10, 6, 5] should return 5 because it appeared first). If there is no mode return -1. The array will not be empty.

def SimpleMode(arr):
  counts = {}
  max_counts = 1
  modes = []
  for n in arr:
    if n in counts:
      counts[n] += 1
      if counts[n] > max_counts:
        max_counts = counts[n]
        modes = [n]
      elif counts[n] == max_counts:
        modes.append(n)
    else:
      counts[n] = 1
  if len(modes) == 0:
    return -1
  # If there are multiple modes, we return the one with the lowest index in the original arr
  return sorted(modes, key=lambda a: arr.index(a))[0]
