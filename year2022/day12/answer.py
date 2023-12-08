import os
from pprint import pp


def get_value(value: str):
    match value:
        case "S":
            value = "a"
        case "E":
            value = "z"
        case _:
            value = value
    return value


def is_valid_move(current_value: str, next_value: str):
    return ord(get_value(next_value)) - ord(get_value(current_value)) <= 1


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    grid = [x.strip() for x in f.readlines()]

stack = []
visited = []

elements = len(grid) * len(grid[0])
scores = [[elements + 1 for _ in range(0, len(grid[0]))] for _ in range(0, len(grid))]

# Find starting position
row = ["S" in line for line in grid].index(True)
col = grid[row].find("S")
scores[row][col] = 0
stack.append((row, col))

while stack:
    current_pos = stack.pop(0)
    row, col = current_pos
    if current_pos in visited:
        continue

    for shift_row, shift_col in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if not 0 <= row + shift_row < len(grid) or not 0 <= col + shift_col < len(grid[0]):
            continue
        if not is_valid_move(grid[row][col], grid[row + shift_row][col + shift_col]):
            continue
        scores[row + shift_row][col + shift_col] = min(
            scores[row + shift_row][col + shift_col], scores[row][col] + 1
        )
        stack.append((row + shift_row, col + shift_col))

    visited.append(current_pos)

end_row = ['E' in line for line in grid].index(True)
end_col = grid[end_row].find("E")

print(f"Puzzle 1: {scores[end_row][end_col]}")