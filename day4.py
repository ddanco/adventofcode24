from itertools import chain
from typing import List, Tuple


##############
### Part 1 ###
##############

def line_count(line: str) -> int:
	count = 0
	for i in range(len(line) - 3):
		if 'XMAS' in (line[i:i+4], line[i:i+4][::-1]):
			count += 1
	return count

def get_diagonals(rows: List[str]) -> List[str]:
	levels: Tuple[str, ...] = tuple()
	for row in range(len(rows)*2):
		level: List[str] = []
		for c in range(row + 1):
			if row-c < len(rows) and c < len(rows[row-c]):
				level += rows[row-c][c]
		levels += (''.join(level),)

	return list(levels)

def get_xmas_count(input: str) -> int:
	rows = input.split('\n')
	columns = [''.join(row[i] for row in rows) for i in range(len(rows[0]))]

	diagonals_ltr_up = get_diagonals(rows)
	# Reverse all strings to get the other diagonals
	diagonals_ltr_down = get_diagonals([string[::-1] for string in rows])

	return sum(line_count(line)
			for line in chain(rows, columns, diagonals_ltr_up, diagonals_ltr_down))

#################

if __name__ == "__main__":

	input = """..."""

	print(f'XMAS count: {get_xmas_count(input)}')
