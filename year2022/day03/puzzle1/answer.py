import os
import sys
sys.path.append(os.getcwd())
from year2022.day3.shared import get_score

ans = 0


def get_shared_character(line: str):
    line = line.strip()
    if len(line) % 2 != 0:
        raise Exception(f"Line should have even number length: {line}")

    first_part = line[0 : int(len(line) / 2)]
    character = [x for x in first_part]

    second_part = line[int(len(line) / 2) :]
    for x in second_part:
        if x in character:
            return x
    raise Exception("Two parts has no shared character")


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for line in f:
        ans += get_score(get_shared_character(line))

print(ans)
