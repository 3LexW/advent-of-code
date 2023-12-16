from functools import cache
import os
import re
from pprint import pp

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    map = [x.replace("\n", "") for x in f.readlines() if len(x.strip()) > 0]


movements = re.findall(r"(\d+)([LR])?", map.pop())

# Add the missing spaces
max_length = max([len(row) for row in map])
for i in range(len(map)):
    map[i] = map[i] + (" " * (max_length - len(map[i])))

directions = ["right", "down", "left", "up"]
row = [i for i, row in enumerate(map) if "." in row][0]
col = [i for i, col in enumerate(map[row]) if col == "."][0]
direction = 0


@cache
def get_row_end_cols(row: int):
    """Return the both ends col index of a row of the map"""
    global map
    has_values = [i for i, x in enumerate(map[row]) if x != " "]
    return has_values[0], has_values[-1]


@cache
def get_col_end_rows(col: int):
    """Return the both ends row index of a column of the map"""
    global map
    col = [line[col] for line in map]
    has_values = [i for i, x in enumerate(col) if x != " "]
    return has_values[0], has_values[-1]


@cache
def get_next_position(current_row: int, current_col: int, direction: int):
    global map, directions
    if map[current_row][current_col] not in ".":
        raise Exception("Current position is not a valid position")

    row_shift = [0, 1, 0, -1][direction]
    col_shift = [1, 0, -1, 0][direction]

    next_row = current_row + row_shift
    next_col = current_col + col_shift

    # Out of bound, move to the other end
    match directions[direction]:
        case "up":
            if next_row < get_col_end_rows(next_col)[0]:
                next_row = get_col_end_rows(next_col)[1]
        case "down":
            if next_row > get_col_end_rows(next_col)[1]:
                next_row = get_col_end_rows(next_col)[0]
        case "left":
            if next_col < get_row_end_cols(next_row)[0]:
                next_col = get_row_end_cols(next_row)[1]
        case "right":
            if next_col > get_row_end_cols(next_row)[1]:
                next_col = get_row_end_cols(next_row)[0]

    if map[next_row][next_col] != "#":
        return next_row, next_col
    else:
        return current_row, current_col


for step, turn in movements:
    for _ in range(int(step)):
        next_row, next_col = get_next_position(row, col, direction)
        if (row, col) == (next_row, next_col):
            break  # Early escape
        row, col = next_row, next_col

    # Change direction
    match turn:
        case "L":
            direction -= 1
        case "R":
            direction += 1
        case _:
            pass
    direction %= len(directions)

print(f"Puzzle 1: {1000 * (row + 1) + 4 * (col + 1) + direction}")
