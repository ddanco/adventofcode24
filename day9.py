

def convert_input_to_blocks(input: str) -> str:
  digits = tuple(int(x) for x in list(input))
  blocks = ''
  for i, d in enumerate(digits):
    if i % 2 == 0:
      blocks += str(i//2)*d
    else:
      blocks += '.'*d
  return blocks

def move_file_blocks(blocks: str) -> str:
  while not all(x == '.' for x in list(blocks[blocks.find('.'):])):
    digit_index = -1
    for i, c in enumerate(list(reversed(blocks))):
      if c.isdigit():
        next_digit, digit_index = c, len(blocks)-1-i
        break
    dot_index = blocks.find('.')
    blocks = blocks[:dot_index] + next_digit + \
        blocks[dot_index+1:digit_index] + '.' + blocks[digit_index+1:]

  return blocks

def get_check_sum(i: str) -> int:
  finalized_block_string = move_file_blocks(convert_input_to_blocks(input))
  return sum(i*int(c) for i, c in
      enumerate(tuple(filter(lambda c: c.isdigit(), list(finalized_block_string)))))


if __name__ == '__main__':

  input = '''...'''
  print(f'Check sum: {get_check_sum(input)}')