from itertools import chain
from typing import Tuple


##############
### Part 1 ###
##############

def fill_map_iter(grid: list[str]) -> list[str]:

  def complete(loc, guard) -> bool:
    return loc[0] == 0 and guard == '^' or \
        loc[0] == len(grid) - 1 and guard == 'v' or \
        loc[1] == 0 and guard == '<' or \
        loc[1] == len(grid[0]) - 1 and guard == '>'

  loc = get_loc_of_guard(grid)
  guard = grid[loc[0]][loc[1]]

  rotations = {
      '^': '>',
      'v': '<',
      '>': 'v',
      '<': '^'}

  while not(complete(loc, guard)):
    if guard == '^':
      next_pos = (loc[0]-1, loc[1])
    elif guard == 'v':
      next_pos = (loc[0]+1, loc[1])
    elif guard == '>':
      next_pos = (loc[0], loc[1]+1)
    else:
      assert guard == '<'
      next_pos = (loc[0], loc[1]-1)

    if grid[next_pos[0]][next_pos[1]] == '#':
      grid[loc[0]] = grid[loc[0]].replace(guard, rotations[guard])
      guard = rotations[guard]
      continue

    grid[loc[0]] = grid[loc[0]][:loc[1]] + 'X' + grid[loc[0]][loc[1]+1:]
    grid[next_pos[0]] = grid[next_pos[0]][:next_pos[1]] + guard + grid[next_pos[0]][next_pos[1]+1:]
    loc = next_pos

  grid[loc[0]] = grid[loc[0]].replace(guard, 'X')
  return grid

def get_loc_of_guard(grid: list[str]) -> Tuple[int, int]:
  for i, row in enumerate(grid):
    for c in ('^', '>', 'v', '<'):
      j = row.find(c)
      if j > -1:
        guard = (i, j)
        break
  assert guard
  return guard

def get_num_spaces_visited(input: str) -> int:
  grid_rows = input.split('\n')
  filled_map = fill_map_iter(grid_rows)
  return len(tuple(filter(lambda char: char == 'X', chain(*filled_map))))


if __name__ == '__main__':

  input = '''...'''

  print(f'Number of spaces visited: {get_num_spaces_visited(input)}')
