import os
from pprint import pp
from typing import List, Set, Tuple

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    map = [x.strip() for x in f.readlines()]


def visited_coordinates(visited: List[Tuple[int, int, str]]) -> Set[Tuple[int, int]]:
    return set([(r, c) for r, c, _ in visited])


def print_energized(map: List[str], visited: List[Tuple[int, int, str]]) -> None:
    map2 = []
    visited = visited_coordinates(visited)

    for r in range(len(map)):
        map2.append("")
        for c in range(len(map[0])):
            if (r, c) in visited:
                map2[r] += "#"
            else:
                map2[r] += "."
    pp(map2)


def visit_map(map: List[str], from_row: int, from_col: int, from_direction: str) -> int:
    stack = [(from_row, from_col, from_direction)]
    visited = set()

    while stack:
        row, col, direction = stack.pop()

        if (row, col, direction) in visited:
            continue

        if not (0 <= row < len(map) and 0 <= col < len(map[0])):
            continue  # Out of bound

        r_shift, c_shift = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }[direction]

        match map[row][col]:
            case ".":
                stack.append((row + r_shift, col + c_shift, direction))  # Continue
            case "|":
                if direction in ["up", "down"]:
                    stack.append((row + r_shift, col + c_shift, direction))  # Continue
                else:
                    # Split
                    stack.append((row - 1, col, "up"))
                    stack.append((row + 1, col, "down"))
            case "-":
                if direction in ["left", "right"]:
                    stack.append((row + r_shift, col + c_shift, direction))  # Continue
                else:
                    # Split
                    stack.append((row, col - 1, "left"))
                    stack.append((row, col + 1, "right"))
            case "/":
                r_shift, c_shift, next_direction = {
                    "up": (0, 1, "right"),
                    "right": (-1, 0, "up"),
                    "down": (0, -1, "left"),
                    "left": (1, 0, "down"),
                }[direction]
                stack.append((row + r_shift, col + c_shift, next_direction))
            case "\\":
                r_shift, c_shift, next_direction = {
                    "up": (0, -1, "left"),
                    "left": (-1, 0, "up"),
                    "down": (0, 1, "right"),
                    "right": (1, 0, "down"),
                }[direction]
                stack.append((row + r_shift, col + c_shift, next_direction))

        visited.add((row, col, direction))
    return len(visited_coordinates(visited))


print(f"Puzzle 1: {visit_map(map, 0, 0, 'right')}")

max_result = 0
start_positions = (
    [(i, 0, "right") for i in range(len(map))]
    + [(i, len(map[0]) - 1, "left") for i in range(len(map))]
    + [(0, i, "down") for i in range(len(map[0]))]
    + [(len(map) - 1, i, "up") for i in range(len(map[0]))]
)

for r, c, p in start_positions:
    max_result = max(max_result, visit_map(map, r, c, p))

print(f"Puzzle 2: {max_result}")
