import os
import sys
from typing import List

sys.path.append(os.getcwd())
from year2022.day3.shared import get_score


def get_shared_character(lines: List[str]):
    line1_chars = [char for char in lines[0].strip()]
    line2_shared = [char for char in lines[1].strip() if char in line1_chars]
    line3_shared = [char for char in lines[2].strip() if char in line2_shared]
    return line3_shared[0]


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    lines = f.readlines()

if len(lines) % 6 != 0:
    raise Exception("File's line should be the multiple of 6")

chunks = [lines[i : i + 3] for i in range(0, len(lines), 3)]
# Split each entry into two entries, three for each
scores = [get_score(get_shared_character(chunk)) for chunk in chunks]
print(sum(scores))
