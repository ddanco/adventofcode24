import copy


def convert_level(raw_level: str) -> list[int]:
  return [int(num) for num in raw_level.split(' ')]

def strictly_increasing_or_decreasing(level: list[int]) -> bool:
  return len(level) == len(list(set(level))) and \
      (level == sorted(level) or level == sorted(level, reverse=True))

def jumps_legal(level: list[int]) -> bool:
  return not any(abs(level[i] - level[i+1]) > 3 for i in range(len(level) - 1))

def level_safe(level: list[int]) -> bool:
  return strictly_increasing_or_decreasing(level) and jumps_legal(level)

def level_safe_with_dampening(level:list[int]) -> bool:
  return any(level_safe(level[:i] + level[i+1:]) for i in range(len(level)))

### Part 1 ###

def safe_count(input: str) -> int:
  levels = input.split('\n')
  return len(list(filter(lambda level: level_safe(convert_level(level)), levels)))

### Part 2 ###

def safe_count_with_dampening(input: str) -> int:
  levels = input.split('\n')
  return len(list(filter(lambda level: level_safe_with_dampening(convert_level(level)), levels)))

##############

if __name__ == "__main__":

  input = '''...'''

  print(f'Number of safe levels: {safe_count(input)}')
  print(f'Number of safe levels with dampening: {safe_count_with_dampening(input)}')
