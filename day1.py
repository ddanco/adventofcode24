from typing import Dict, Tuple


##############
### Part 1 ###
##############


def sorted_lists(input: str) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
  lines = tuple(line.split('   ') for line in input.split('\n'))
  sortable_lines = tuple((int(a), int(b)) for (a, b) in lines)
  first, second = zip(*sortable_lines)

  return (tuple(sorted(first)), tuple(sorted(second)))


def total_distance(input: str) -> int:
  first_list, second_list = sorted_lists(input)
  zipped = zip(first_list, second_list)

  difference = lambda pair: abs(pair[0] - pair[1])

  return sum(difference(pair) for pair in zipped)


##############
### Part 2 ###
##############


def get_counts(sorted_list: Tuple[int, ...]) -> Dict[int, int]:
  assert len(sorted_list) > 0
  counts, cur, count = {}, sorted_list[0], 0
  for x in sorted_list:
    if x == cur:
      count += 1
    else:
      counts[cur], cur, count = count, x, 1
  counts[cur] = count
  return counts


def similarity_score(input: str) -> int:
  first_list, second_list = sorted_lists(input)
  counts = get_counts(second_list)

  return sum(counts.get(number, 0) * number for number in first_list)


##############


if __name__ == "__main__":

  input = '''...'''

  print(f'Total distance: {total_distance(input)}')
  print(f'Similarity score: {similarity_score(input)}')
