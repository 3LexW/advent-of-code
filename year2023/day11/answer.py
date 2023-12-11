import os
from typing import List
from itertools import combinations

grid: List[List[str]] = []
empty_rows = set()
empty_cols = set()

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for i, row in enumerate(f):
        grid.append(list(row.strip()))
        if "#" not in row:
            empty_rows.add(i)

for col in range(len(grid[0]) - 1, -1, -1):
    if "#" not in [row[col] for row in grid]:
        empty_cols.add(col)

galaxies = set()
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == "#":
            galaxies.add((row, col))


def get_distance(r1: int, c1: int, r2: int, c2: int):
    global grid, empty_rows, empty_cols, multiplier
    extra_row = (multiplier - 1) * len(
        [x for x in range(min(r1, r2), max(r1, r2)) if x in empty_rows]
    )
    extra_col = (multiplier - 1) * len(
        [x for x in range(min(c1, c2), max(c1, c2)) if x in empty_cols]
    )
    return abs(r1 - r2) + abs(c1 - c2) + extra_row + extra_col


pairs = list(combinations(galaxies, 2))

multiplier = 2
ans = sum([get_distance(r1, c1, r2, c2) for (r1, c1), (r2, c2) in pairs])
print(f"Puzzle 1: {ans}")

multiplier = 1000000
ans = sum([get_distance(r1, c1, r2, c2) for (r1, c1), (r2, c2) in pairs])
print(f"Puzzle 2: {ans}")
