import os
import re
import sys
from typing import List

p1 = 0
p2 = 0


def p1_combinations(numbers: List[int], target: int) -> bool:
    if len(numbers) == 1:
        return numbers[0] == target

    # Take the left most numbers
    left = numbers.pop(0)
    right = numbers.pop(0)

    plus = numbers.copy()
    plus.insert(0, left + right)
    times = numbers.copy()
    times.insert(0, left * right)

    return p1_combinations(plus, target) or p1_combinations(times, target)


def p2_combinations(numbers: List[int], target: int) -> bool:
    if len(numbers) == 1:
        return numbers[0] == target

    # Take the left most numbers
    left = numbers.pop(0)
    right = numbers.pop(0)

    if left > target:
        return False # Early escape since the number can only get bigger

    plus = numbers.copy()
    plus.insert(0, left + right)
    times = numbers.copy()
    times.insert(0, left * right)
    join = numbers.copy()
    join.insert(0, int(f"{left}{right}"))

    return (
        p2_combinations(plus, target)
        or p2_combinations(times, target)
        or p2_combinations(join, target)
    )


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for line in f.readlines():
        target, numbers = re.findall(r"(\d+): (.*)", line)[0]
        target = int(target)
        numbers = list(map(int, numbers.split()))

        if p1_combinations(numbers.copy(), target):
            p1 += target
        if p2_combinations(numbers.copy(), target):
            p2 += target

print(f"Puzzle 1: {p1}")
print(f"Puzzle 2: {p2}")
