from itertools import chain


##############
### Part 1 ###
##############

def line_count(line: str) -> int:
  return sum('XMAS' in (line[i:i+4], line[i:i+4][::-1]) for i in range(len(line)-3))

def get_diagonals(rows: list[str]) -> list[str]:
  return list(chain.from_iterable((''.join(rows[row-c][c] for c in range(row+1)
      if row-c < len(rows) and c < len(rows[row-c])),) for row in range(len(rows)*2)))

def get_xmas_count(input: str) -> int:
  rows = input.split('\n')
  columns = [''.join(row[i] for row in rows) for i in range(len(rows[0]))]

  diagonals_ltr_up = get_diagonals(rows)
  # Reverse all strings to get the other diagonals
  diagonals_ltr_down = get_diagonals([string[::-1] for string in rows])

  return sum(line_count(line)
      for line in chain(rows, columns, diagonals_ltr_up, diagonals_ltr_down))

##############
### Part 2 ###
##############

def has_masmas(square: list[str]) -> bool:
  l1, l2, l3 = square

  return l2[1] == 'A' and any((
      l1[0] == l1[2] == 'M' and l3[0] == l3[2] == 'S',
      l1[0] == l1[2] == 'S' and l3[0] == l3[2] == 'M',
      l1[0] == l3[0] == 'M' and l1[2] == l3[2] == 'S',
      l1[0] == l3[0] == 'S' and l1[2] == l3[2] == 'M'))

def get_masmas_count(input: str) -> int:
  rows = input.split('\n')
  squares = tuple([rows[i][j:j+3], rows[i+1][j:j+3], rows[i+2][j:j+3]]
      for i in range(len(rows)-2) for j in range(len(rows[0])-2))

  return len(tuple(filter(lambda s: has_masmas(s), squares)))

###############

if __name__ == "__main__":

  input = """..."""

  print(f'XMAS count: {get_xmas_count(input)}')
  print(f'MASMAS count: {get_masmas_count(input)}')
