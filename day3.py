import re


def get_product(match: str) -> int:
    split_elems = match[4:-1].split(',')
    return int(split_elems[0]) * int(split_elems[1])

def calculate_uncorrupted(text: str) -> int:
    matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", text)
    return sum(get_product(match) for match in matches)


if __name__ == "__main__":

    input = """..."""

    print(f'Sum of uncorrupted products is: {calculate_uncorrupted(input)}')
