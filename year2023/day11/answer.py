import os
from typing import List
from itertools import combinations

grid: List[List[str]] = []
with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for row in f:
        grid.append(list(row.strip()))
        if "#" not in row:
            grid.append(list(row.strip()))  # expand

for col in range(len(grid[0]) - 1, -1, -1):
    if "#" not in [row[col] for row in grid]:
        for row in range(len(grid)):
            grid[row].insert(col + 1, ".")

galaxies = set()
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == "#":
            galaxies.add((row, col))

pairs = list(combinations(galaxies, 2))
ans1 = sum([abs(r1 - r2) + abs(c1 - c2) for (r1, c1), (r2, c2) in pairs])

print(f"Puzzle 1: {ans1}")
