# Have the function SudokuQuadrantChecker(strArr) read the strArr parameter being passed which will represent a 9x9 Sudoku board of integers 
# ranging from 1 to 9. The rules of Sudoku are to place each of the 9 integers integer in every row and column and not have any integers repeat 
# in the respective row, column, or 3x3 sub-grid. The input strArr will represent a Sudoku board and it will be structured in the following format: 
# ["(N,N,N,N,N,x,x,x,x)","(...)","(...)",...)] where N stands for an integer between 1 and 9 and x will stand for an empty cell. Your program will 
# determine if the board is legal; the board also does not necessarily have to be finished. If the board is legal, your program should return the 
# string legal but if it isn't legal, it should return the 3x3 quadrants (separated by commas) where the errors exist. The 3x3 quadrants are numbered 
# from 1 to 9 starting from top-left going to bottom-right.

import re
def SudokuQuadrantChecker(strArr):
  # Turn the list of strings into a list of lists of characters
  list_list = [list(re.findall(r'\d+|x', row)) for row in strArr]
  # Tracks repeats, with keys being the row and column of the repeat, as 'r-c'
  repeats = {}
  # check rows for repeats
  for r in range(9):
    counts = {}
    for c in range(9):
      if list_list[r][c].isnumeric() and list_list[r][c] in counts:
        repeats[f'{r}-{c}'] = True
        repeats[counts[list_list[r][c]]] = True
      elif list_list[r][c].isnumeric():
        counts[list_list[r][c]] = f'{r}-{c}'
  # check columns for repeats
  for c in range(9):
    counts = {}
    for r in range(9):
      if list_list[r][c].isnumeric() and list_list[r][c] in counts:
        repeats[f'{r}-{c}'] = True
        repeats[counts[list_list[r][c]]] = True
      elif list_list[r][c].isnumeric():
        counts[list_list[r][c]] = f'{r}-{c}'
  # check quadrants for repeats
  for c in range(0,9,3):
    for r in range(0,9,3):
      counts = {}
      for qc in range(c, c+3):
        for qr in range(r, r+3):
          if list_list[qr][qc].isnumeric() and list_list[qr][qc] in counts:
            repeats[f'{qr}-{qc}'] = True
            repeats[counts[list_list[qr][qc]]] = True
          elif list_list[qr][qc].isnumeric():
            counts[list_list[qr][qc]] = f'{qr}-{qc}'
  
  # If there are no repeats, return 'legal'
  if len(repeats) == 0:
    return 'legal'

  # This calculates what quadrant each repeat is in
  quadrants = [3 * int(int(val[0]) / 3) + 1 + int(int(val[2]) / 3) for val in repeats.keys()]
  
  # We need to first remove repeated repeats, then sort repeats, then join them
  return ','.join(map(str, (sorted(set(quadrants)))))
