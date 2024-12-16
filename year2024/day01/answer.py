import os
import re

left = []
right = []

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for line in f.readlines():
        format = R'(\d+) *(\d+)'
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)

    left1 = left.copy()
    right1 = right.copy()

    left1.sort()
    right1.sort()

    p1 = [abs(l - r) for l, r in zip(left1, right1)]
    print(f"Puzzle 1: {sum(p1)}")

    p2 = [l * right.count(l) for l, r in zip(left, right)]
    print(f"Puzzle 2: {sum(p2)}")