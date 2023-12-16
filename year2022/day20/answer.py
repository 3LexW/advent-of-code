from copy import deepcopy
import os
from typing import List, Tuple


def get_index_by_order(lines: List[Tuple[int, int]], order: int) -> int:
    return [i for i, (o, _) in enumerate(lines) if order == o][0]


def get_index_by_movement(lines: List[Tuple[int, int]], movement: int) -> int:
    return [i for i, (_, m) in enumerate(lines) if movement == m][0]


def get_result(lines: List[Tuple[int, int]]) -> int:
    index0 = get_index_by_movement(lines, 0)
    ans = 0
    for i in range(1000, 4000, 1000):
        value = lines[(index0 + i) % len(lines)][1]
        print(f"{i}th value: {value}")
        ans += value
    return ans


def mix_lines(lines: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    for i in range(len(lines)):
        index = get_index_by_order(lines, i)
        (order, movement) = lines[index]

        lines.pop(index)
        next_index = index + movement
        while next_index < 0 or next_index >= len(lines):
            next_index %= len(lines)
        if next_index == 0:
            next_index = len(lines)

        lines.insert(next_index, (order, movement))
    return lines


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    lines = [(i, int(x.strip())) for i, x in enumerate(f.readlines())]
with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    lines2 = [(i, int(x.strip()) * 811589153) for i, x in enumerate(f.readlines())]

lines = mix_lines(lines)
print(f"Puzzle 1: {get_result(lines)}")

# Round 2
for i in range(0, 10):
    print(f"Mixing lines2: Loop {i + 1}")
    lines2 = mix_lines(lines2)
print(f"Puzzle 2: {get_result(lines2)}")
