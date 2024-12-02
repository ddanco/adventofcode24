from typing import Tuple


def total_distance(input: str) -> int:

  def get_sorted_lists(input: str) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
    lines = input.split('\n')
    first = tuple(int(line.split('   ')[0]) for line in lines)
    second = tuple(int(line.split('   ')[-1]) for line in lines)

    return (tuple(sorted(first)), tuple(sorted(second)))

  first_list, second_list = get_sorted_lists(input)
  assert(len(first_list) == len(second_list))
  zipped = zip(first_list, second_list)

  get_difference = lambda pair: abs(pair[0] - pair[1])

  return sum(get_difference(pair) for pair in zipped)


if __name__ == "__main__":

  input = ...

  print(f'Total distance: {total_distance(input)}')
