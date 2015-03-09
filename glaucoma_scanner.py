#!/usr/bin/python
'''
Problem statement:
  You are given a 10x10 grid as a set of squares. Each square has a row, column, and a score.
  The score can be 1,2,3,4, or 5.
  The task is to find all the contiguous regions of squares made of at least 3 squares of a certain
  score. Whether two squares are contiguous is defined by whether the squares have touching
  edges or corners.
  Each contigues region of squares must meet two requirements in order to be considered a
  contigous region:
    - The region can contain no squares that have score 5.
    - The region can contain only one square that has score 4.

TL;DR Details that are relevant only for the actual glaucoma scan:
  (My sister is a med-student, and she asked me to figure out this algorithm for her project
  which uses a glaucoma scanner).
  Scores correspond to the brightness of lights that flash on the screen while the patent looks
  at the centert of the screen, and identifies locations of flashes if the he or she can see them.)
  A score of 5 is dimmest flash, 1 is brightest flash.
  A square is given the score of the dimmest brightness the patient can see at that location.
  A contiguous region in the solution is a blind spot the patient has.

Details that are relevant to my solution:
  I've solved this problem as though the origin of the grid is at the top left. To move the origin
    to the center of the grid after solving the problem, simply subtract GRID_SIZE/2 from each
    square's row and column.
  NOTE: This solution has a bug or two in it ;)
'''

GRID_SIZE = 10

EXAMPLE_GRID = \
  "55555455555" + \
  "51555455555" + \
  "55155455555" + \
  "55515555555" + \
  "55555555555" + \
  "55555555555" + \
  "55555455555" + \
  "55555455555" + \
  "55555455555" + \
  "55555455555"

EXAMPLE_GRID_2 = \
  "55555455555" + \
  "55555455555" + \
  "55555455555" + \
  "55555455555" + \
  "55555555555" + \
  "55555555555" + \
  "55555455555" + \
  "55555555555" + \
  "55555455555" + \
  "55555455555"

class Square(object):
  def __init__(self, row, col, score):
    self.row = row
    self.col = col
    self.score = score

  def key(self):
    return str(self.row) + ',' + str(self.col)

  def equalTo(square):
    return square.key == self.key

  def __str__(self):
    return str(self.row) + ',' + str(self.col) + ' score: ' + str(self.score)

# Build a hashmap to hold the squares. They key is "row,col", e.g. "3,4", and the
# value is the square's score.
squares = {}
for row in range(GRID_SIZE):
  for col in range(GRID_SIZE):
    squares[str(row) + ',' + str(col)] = Square(int(row), int(col), int(EXAMPLE_GRID[GRID_SIZE*row + col]))

def get_neighbors(grid, row, col):
  '''
  Returns a list of Square objects that are neighbors of (aka contiguous to) the square
  at the given row and col.
  '''
  neighbors = []
  for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
      # A square cannot be a neighbor of itself
      if dx == 0 and dy == 0:
        continue

      # Check whether the square is on the board
      if row + dy < 0 or row + dy >= GRID_SIZE:
        continue
      if col + dx < 0 or col + dx >= GRID_SIZE:
        continue

      neighbors.append(squares[str(row + dy) + ',' + str(col + dx)])
  return neighbors

def get_non_chosen_neighbors_of_score_4_or_less(neighbors, already_chosen):
  return [square for square in neighbors if square.score <= 4 \
                                        and square.key not in already_chosen]

# First, find the contiguous region
print 'Just testing to make sure get_neighbors is correct:'
print 'Neighbors of 2,9:'
for n in get_neighbors(EXAMPLE_GRID, 2, 9):
  print n

print 'Neighbors of 5,5:'
for n in get_neighbors(EXAMPLE_GRID, 5, 5):
  print n

# Heh, this solution is actually recursive, because I anticipate that you'll want
# maximally-sized regions, not just regions of length 3.
def region_containing_square_and_possibly_many_fours(square, squares_already_chosen):
  neighbors = get_non_chosen_neighbors_of_score_4_or_less(
    get_neighbors(EXAMPLE_GRID, square.row, square.col),
    squares_already_chosen)

  if len(neighbors) == 0:
    return []

  result = []
  for neighbor in neighbors:
    result.extend(region_containing_square_and_possibly_many_fours(neighbor, squares_already_chosen + [square]))
  return result

def contains_more_than_one_four(region):
  num_fours = 0
  for square in region:
    if square.score == 4:
      ++num_fours
      if num_fours > 1:
        return true
  return false

# Here we use recursion again ;)
def contiguous_regions_containing_square(square, region_possibly_containing_fours):
  '''
  Tries every possible combination of how we could remove 4's. If the region is large and has
  many fours, and the candidate region is large, this could be computationally infeasible,
  unless we add the optimization that we first remove the outermost squares (squares that
  don't divide the region if they're eliminated) that have a score of 4.
  '''
  if not contains_more_than_one_four(region_possibly_containing_fours):
    return [region_possibly_containing_fours]

  contiguous_regions = []
  for s in region_possibly_containing_fours:
    if s.score == 4 and not square.equalTo(s):
      region_without_s = [sq for sq in region_possibly_containing_fours if not sq.equalTo(s)]
      contiguous_regions.extend(contiguous_regions_containing_square(
        square, region_possibly_containing_fours))
  return contiguous_regions

def region_description(region):
  '''
  Returns a string of square coordinates in the region, along with each square's score.
  The squares are sorted first by row, second by column, so that duplicate solutions
  are not added to the solution-set twice.
  '''
  sorted_squares = sorted(region, key=lambda square: GRID_SIZE*square.row + square.col)
  result = ''
  for square in sorted_squares:
    result.append(square.key + ':' + square.score + ' ')

# `solutions` is a set of qualifying contiguous regions.
solutions = set()
for row in range(GRID_SIZE):
  for col in range(GRID_SIZE):
    square = squares[str(row) + ',' + str(col)]
    if square.score == 1:
      import pdb; pdb.set_trace()
    region = region_containing_square_and_possibly_many_fours(square, [])
    if len(region) >= 3:
      for contiguous_region in \
        contiguous_regions_containing_square(squares[str(row) + ',' + str(col)], region):
        solutions.add(region_description(contiguous_region))

for solution in solutions:
  print solution
