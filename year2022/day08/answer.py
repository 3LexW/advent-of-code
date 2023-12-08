import os
from typing import Set, Tuple
from functools import reduce

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    grid = [l.strip() for l in f.readlines()]

total_rows = len(grid)
total_columns = len(grid[0])

valid: Set[Tuple[int, int]] = set()


def edge_check(row, column, total_rows, total_columns):
    return (
        True
        if row == 0
        or row == total_rows - 1
        or column == 0
        or column == total_columns - 1
        else False
    )


for row in range(0, total_rows):
    # Get the edge values
    for column in range(0, total_columns):
        if edge_check(row, column, total_rows, total_columns):
            valid.add((row, column))
            continue

    line = grid[row]

    # Scan from left to right, if valid, add to valid list
    row_max = 0
    for column in range(0, total_columns):
        value = int(grid[row][column])
        if value > row_max:
            valid.add((row, column))
        row_max = max(row_max, value)

    # Scan from right to left
    row_max = 0
    for column in range(total_columns - 1, -1, -1):
        value = int(grid[row][column])
        if value > row_max:
            valid.add((row, column))
        row_max = max(row_max, value)

for column in range(0, total_columns):
    line = "".join([row[column] for row in grid])
    # Scan from top to bottom
    column_max = 0
    for row in range(0, total_rows):
        value = int(grid[row][column])
        if value > column_max:
            valid.add((row, column))
        column_max = max(column_max, value)

    # Scan from bottom to top
    column_max = 0
    for row in range(total_rows - 1, -1, -1):
        value = int(grid[row][column])
        if value > column_max:
            valid.add((row, column))
        column_max = max(column_max, value)


print(f"Puzzle 1: {len(valid)}")


# Puzzle 2
max_score = 0

for row in range(0, total_rows):
    for column in range(0, total_columns):
        value = grid[row][column]
        if edge_check(row, column, total_rows, total_columns):
            score = 0
        else:
            left, right, top, bottom = 1, 1, 1, 1
            while column - left > 0 and grid[row][column - left] < value:
                left += 1
            while (
                column + right < total_columns - 1 and grid[row][column + right] < value
            ):
                right += 1
            while row - top > 0 and grid[row - top][column] < value:
                top += 1
            while row + bottom < total_rows - 1 and grid[row + bottom][column] < value:
                bottom += 1
            score = reduce(lambda a, b: a * b, list([left, right, top, bottom]))

        max_score = max(max_score, score)

print(f"Puzzle 2: {max_score}")
