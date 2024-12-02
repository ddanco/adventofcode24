from typing import Dict, Tuple


##############
### Part 1 ###
##############


def sorted_lists(input: str) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
  lines = input.split('\n')
  first = tuple(int(line.split('   ')[0]) for line in lines)
  second = tuple(int(line.split('   ')[-1]) for line in lines)

  return (tuple(sorted(first)), tuple(sorted(second)))


def total_distance(input: str) -> int:
  first_list, second_list = sorted_lists(input)
  assert(len(first_list) == len(second_list))
  zipped = zip(first_list, second_list)

  difference = lambda pair: abs(pair[0] - pair[1])

  return sum(difference(pair) for pair in zipped)


##############
### Part 2 ###
##############


def get_counts(sorted_list: Tuple[int, ...]) -> Dict[int, int]:
  counts = {}
  assert len(sorted_list) > 0
  cur = sorted_list[0]
  count = 0
  for x in sorted_list:
    if x == cur:
      count += 1
    else:
      counts[cur] = count
      cur, count = x, 1
  counts[cur] = count
  return counts


def similarity_score(input: str) -> int:
  first_list, second_list = sorted_lists(input)
  counts = get_counts(second_list)

  def similarity_value(number: int) -> int:
    if number in counts:
      return counts[number] * number
    return 0

  return sum(similarity_value(number) for number in first_list)


##############


if __name__ == "__main__":

  input = ...

  print(f'Total distance: {total_distance(input)}')
  print(f'Similarity score: {similarity_score(input)}')
