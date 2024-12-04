import re

from typing import Tuple


def get_product(match: str) -> int:
  split_elems = match[4:-1].split(',')
  return int(split_elems[0]) * int(split_elems[1])

### Part 1 ###

def calculate_uncorrupted(text: str) -> int:
  matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", text)
  return sum(get_product(match) for match in matches)

### Part 2 ###

def calculate_enabled_multiplications(text: str) -> int:
  def helper(params: Tuple[str, int]) -> Tuple[str, int]:
    text, acc = params
    stop_point = text.find("don't()")
    next_start_point = text.find("do()", stop_point)
    updated_sum = calculate_uncorrupted(text[:stop_point]) + acc
    if next_start_point == -1:
      return ('', updated_sum)
    return helper((text[next_start_point:], updated_sum))
  _, acc = helper((text + "don't()", 0))
  return acc

##############

if __name__ == "__main__":

  input = '''...'''

  print(f'Sum of uncorrupted: {calculate_uncorrupted(input)}')
  print(f'Sum of enabled uncorrupted: {calculate_enabled_multiplications(input)}')
