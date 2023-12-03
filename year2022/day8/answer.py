import os
from typing import Set, Tuple

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

total_rows = len(lines)
total_columns = len(lines[0])

valid: Set[Tuple[int, int]]= set()

def edge_check(row, column, total_rows, total_columns):
    return True if row == 0 or row == total_rows - 1 or column == 0 or column == total_columns - 1 else False

for row in range(0, total_rows):
    # Get the edge values
    for column in range(0, total_columns):
        if edge_check(row, column, total_rows, total_columns):
            valid.add((row, column)) 
            continue

    line = lines[row]

    # Scan from left to right, if valid, add to valid list
    row_max = 0
    for column in range(0, total_columns):
        value = int(lines[row][column])
        if value > row_max:
            valid.add((row, column))
        row_max = max(row_max, value)
    
    # Scan from right to left
    row_max = 0
    for column in range(total_columns - 1, -1, -1):
        value = int(lines[row][column])
        if value > row_max:
            valid.add((row, column))
        row_max = max(row_max, value)

for column in range(0, total_columns):
    line = ''.join([row[column] for row in lines])
    # Scan from top to bottom
    column_max = 0
    for row in range(0, total_rows):
        value = int(lines[row][column])
        if value > column_max:
            valid.add((row, column))
        column_max = max(column_max, value)

    # Scan from bottom to top
    column_max = 0
    for row in range(total_rows - 1, -1, -1):
        value = int(lines[row][column])
        if value > column_max:
            valid.add((row, column))
        column_max = max(column_max, value)


print(f"Puzzle 1: {len(valid)}")