from itertools import chain
from typing import List


def line_count(line: str) -> int:
	count = 0
	for i in range(len(line) - 3):
		if line[i:i+4] == 'XMAS':
			count += 1
	return count

def get_xmas_count(input: str) -> List[List[str]]:
	rows = input.split('\n')
	columns = [''.join(row[i] for row in rows) for i in range(len(rows[0]))]


	def get_diagonals() -> List[str]:
		levels = tuple()
		# for row in range(len(rows)):
		# 	level = []
		# 	for c in range(row + 1):
		# 		level += rows[row-c][c]
		# 	levels += (''.join(level),)

		rows_range = range(len(rows)-1, 0, -1)
		for i, row in enumerate(rows_range):
			level = []
			for c in range(len(rows), len(rows)-i):
			# for c in range(len(rows)-i-1, -1, -1):
				level += rows[row-c][c]
			levels += (''.join(level),)

	get_diagonals()
	return sum(line_count(line) for line in chain(rows, columns))

	# 0: 00
	# 1: 01 10
	# 2: 02 11 20
	# 3: 03 12 21 30
	# c: (r-c)c

	# ....XXMAS.
	# .SAMXMS...
	# ...S..A...
	# ..A.A.MS.X
	# XMASAMX.MM
	# X.....XA.A
	# S.S.S.S.SS
	# .A.A.A.A.A
	# ..M.M.M.MM
	# .X.X.XMASX

if __name__ == "__main__":

	input = """....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX"""

	print(f'XMAS count: {get_xmas_count(input)}')