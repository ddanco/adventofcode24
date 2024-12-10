from typing import Dict, Set, Tuple


def sum_trailhead_scores(input: str, distinct: bool) -> int:
  rows = input.split('\n')
  clean_row = lambda row: list(int(x) for x in list(row))
  grid = list(clean_row(row) for row in rows)
  trailheads = list(filter(lambda coord: grid[coord[0]][coord[1]] == 0,
      [(i, j) for i in range(len(grid)) for j in range(len(grid[0]))]))

  visited: Dict[Tuple[int, int], Set[Tuple[int, int]]] = {t: set() for t in trailheads}

  def walk_trail(trailhead: Tuple[int, int], i: int, j: int, distinct: bool) -> int:
    if grid[i][j] == 9:
      if distinct or ((i, j) not in visited[trailhead]):
        visited[trailhead].add((i, j))
        return 1

    neighbors = [(i-1, j), (i+1, j), (i, j+1), (i, j-1)]
    valid_neighbors = list(filter(lambda c: 0 <= c[0] < len(grid)
        and 0 <= c[1] < len(grid[0]) and grid[c[0]][c[1]] == grid[i][j] + 1,
        neighbors))

    if not valid_neighbors:
      return 0

    return sum(walk_trail(trailhead, *coords, distinct) for coords in valid_neighbors)

  return sum(walk_trail(trailhead, *trailhead, distinct) for trailhead in trailheads)



if __name__ == '__main__':

  input = '''...'''

  print(f'Sum of trailhead scores: {sum_trailhead_scores(input, distinct=False)}')
  print(f'Sum of trailhead ratings: {sum_trailhead_scores(input, distinct=True)}')
