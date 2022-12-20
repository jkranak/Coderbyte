# Have the function OverlappingRectangles(strArr) read the strArr parameter being passed which will represent
# two rectangles on a Cartesian coordinate plane and will contain 8 coordinates with the first 4 making
# up rectangle 1 and the last 4 making up rectange 2. It will be in the following format:
# ["(0,0),(2,2),(2,0),(0,2),(1,0),(1,2),(6,0),(6,2)"] Your program should determine the area of the space
# where the two rectangles overlap, and then output the number of times this overlapping region can fit into
# the first rectangle. For the above example, the overlapping region makes up a rectangle of area rectangle
# of area 2, and the first rectangle (the first 4 coordinates) makes up a rectangle of area 4, so your program
# should output 2. The coordinates will all be integers. If there's no overlap between the two rectangles return 0.

import re
def OverlappingRectangles(strArr):
  def overlap (a, b):
    # We can calculate the overalap between two pairs of numbers by sorting them and then returning the difference 
    # between the middle two values. But this doesn't work if there is no overlap, so we here return 0 for such cases 
    if a[1] < b[0] or b[1] < a[0]:
      return 0
    list_sort = sorted(a + b)
    return list_sort[2] - list_sort[1]
  
  all_nums = list(map(int, re.findall(r'-*\d+', strArr[0])))
  all_xs = all_nums[0::2]
  all_ys = all_nums[1::2]
  xs1 = [min(all_xs[:5]), max(all_xs[:5])]
  xs2 = [min(all_xs[5:]), max(all_xs[5:])]
  ys1 = [min(all_ys[:5]), max(all_ys[:5])]
  ys2 = [min(all_ys[5:]), max(all_ys[5:])]

  area_overlap = overlap(xs1, xs2) * overlap(ys1, ys2)
  if area_overlap == 0:
    return 0
  
  return int((xs1[1] - xs1[0]) * (ys1[1] - ys1[0]) / area_overlap)
