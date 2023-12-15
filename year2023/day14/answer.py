import os
from typing import List
from pprint import pp
from copy import deepcopy


def cal_score(map: List[List[str]]) -> int:
    score = 0
    for i in range(0, len(map)):
        score += (i + 1) * sum([1 for c in map[len(map) - 1 - i] if c == "O"])
    return score


def move_rock(
    map: List[List[str]], row: int, col: int, direction: str
) -> List[List[str]]:
    row_shift, col_shift = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }[direction]

    shift = 1
    while (
        0 <= (row + (shift * row_shift)) < len(map)
        and 0 <= (col + (shift * col_shift)) < len(map[0])
        and map[row + (shift * row_shift)][col + (shift * col_shift)] == "."
    ):
        shift += 1
    shift -= 1

    # Swap the two positions
    map[row][col], map[row + (shift * row_shift)][col + (shift * col_shift)] = (
        map[row + (shift * row_shift)][col + (shift * col_shift)],
        map[row][col],
    )
    return map


def move_map(map: List[List[str]], direction: str) -> List[List[str]]:
    """Based on the direction, the loop moves differently"""
    for r in range(len(map)):
        for c in range(len(map[r])):
            if direction in ("up", "left") and map[r][c] == "O":
                map = move_rock(map, r, c, direction)
            if (
                direction in ("down", "right")
                and map[len(map) - r - 1][len(map[0]) - c - 1] == "O"
            ):
                map = move_rock(map, len(map) - r - 1, len(map[0]) - c - 1, direction)

    return map


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    map = [list(line.strip()) for line in f]


# Shift up and check result
map1 = deepcopy(map)
map1 = move_map(map1, "up")
print(f"Puzzle 1: {cal_score(map1)}")


def flat_map(map: List[List[str]]) -> str:
    return "".join(["".join(line) for line in map])


map2 = deepcopy(map)
history: List[List[str]] = []

for i in range(1000000000 * 4):
    directions = ["up", "left", "down", "right"]
    map2 = move_map(map2, directions[i % len(directions)])

    if map2 not in history:
        history.append(deepcopy(map2))
    else:
        current_step = i + 1
        same_step = history.index(map2) + 1
        loop_size = current_step - same_step
        remaining_steps = same_step + ((1000000000 * 4 - same_step) % loop_size)
        print(f"Found loop in {history.index(map2) + 1 }")
        print(f"Puzzle 2: {cal_score(history[remaining_steps - 1])}")
        exit()
