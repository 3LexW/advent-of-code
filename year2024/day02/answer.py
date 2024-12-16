import os
from typing import List

p1 = 0
p2 = 0


def all_increasing_or_decreasing(line: List[int]) -> bool:
    increasing = line.copy()
    decreasing = line.copy()

    increasing.sort()
    decreasing.sort(reverse=True)
    return increasing == line or decreasing == line


def valid_diff(line: List[int]) -> bool:
    line_copy = line.copy()
    line_copy.sort()

    for i in range(1, len(line_copy)):
        if line_copy[i] - line_copy[i - 1] not in (1, 2, 3):
            return False
    return True


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for line in f.readlines():
        order = list(map(int, line.split()))
        if all_increasing_or_decreasing(order) and valid_diff(order):
            p1 += 1
            p2 += 1
        else:
            for i in range(0, len(order)):
                copy = order.copy()
                copy.pop(i)
                if all_increasing_or_decreasing(copy) and valid_diff(copy):
                    p2 += 1
                    break

    print(f"Puzzle 1: {p1}")
    print(f"Puzzle 2: {p2}")
