# Have the function ShortestPath(strArr) take strArr which will be an array of strings which models a non-looping Graph. 
# The structure of the array will be as follows: The first element in the array will be the number of nodes N (points) 
# in the array as a string. The next N elements will be the nodes which can be anything (A, B, C .. Brick Street, Main Street .. etc.). 
# Then after the Nth element, the rest of the elements in the array will be the connections between all of the nodes. 
# They will look like this: (A-B, B-C .. Brick Street-Main Street .. etc.). Although, there may exist no connections at all.

def ShortestPath(strArr):
  # We first filter out our nodes and edges
  nodes = strArr[1:int(strArr[0])+1]
  edges = [e.split('-') for e in strArr[int(strArr[0])+1:]]
  
  # Paths will serve as a stack for potential paths, starting with any edges that include the first node.
  # Any edge where the first node appears second are resorted so that the first node is always the first value.
  paths = [sorted(e, key=lambda a: a != nodes[0]) for e in edges if nodes[0] in e]
  finished_paths = []
  # We then pop the first path. If there is another edge that can be used to continue the path, we add this longer path to the stack
  while len(paths) > 0:
    path = paeths.pop(0)
    # If a path is finished, it's added to finished_paths and we skip the susequent for loop
    if path[-1] == nodes[-1]:
      finished_paths.append(path)
      continue
    # Here we are seeing if there is an edge that can can continue a given path. If so, we add the node and return it to the paths stack
    for e in edges:
      if int(e[0] in path) != int(e[1] in path):
        if e[0] == path[-1]:
          new_path = [*path, e[1]]
          # We check to make sure a new path isn't already in the paths stack
          if not new_path in paths:
            paths.append(new_path)
        elif e[1] == path[-1]:
          new_path = [*path, e[0]]
          if not new_path in paths:
            paths.append(new_path)

  # If there are no finished paths, we return -1
  if len(finished_paths) == 0:
    return -1

  # This sorts finished paths by length, takes the first one (the shortest), and joins it as a string
  return '-'.join(sorted(finished_paths, key=lambda a: len(a))[0])
