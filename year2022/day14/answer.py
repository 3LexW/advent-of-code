import os, re
from pprint import pp


def get_all_blockers(start, end) -> [(str, str)]:
    start_col, start_row = map(lambda x: int(x), start.split(","))
    end_col, end_row = map(lambda x: int(x), end.split(","))

    x_shift = 1 if end_row > start_row else -1 if end_row < start_row else 0
    y_shift = 1 if end_col > start_col else -1 if end_col < start_col else 0

    shift = 0
    ans = []
    while (
        start_row + shift * x_shift == end_row
        and start_col + shift * y_shift == end_col
    ) == False:
        ans.append((start_row + shift * x_shift, start_col + shift * y_shift))
        shift += 1
    ans.append((end_row, end_col))
    return ans


def get_sand_puzzle_1(start_row, start_col, blockers) -> (int, int):
    current_row, current_col = start_row, start_col
    shifts = [(1, 0), (1, -1), (1, 1)]

    max_row = max([row for row, col in blockers])
    if current_row > max_row:
        return None

    for shift_row, shift_col in shifts:
        if (current_row + shift_row, current_col + shift_col) not in blockers:
            return get_sand_puzzle_1(
                current_row + shift_row, current_col + shift_col, blockers
            )
    return (current_row, current_col)


def get_sand_puzzle_2(start_row, start_col, blockers, max_row):
    current_row, current_col = start_row, start_col
    shifts = [(1, 0), (1, -1), (1, 1)]

    if current_row == max_row:
        return (current_row, current_col)

    for shift_row, shift_col in shifts:
        if (current_row + shift_row, current_col + shift_col) not in blockers:
            return get_sand_puzzle_2(current_row + shift_row, current_col + shift_col, blockers, max_row)
    return (current_row, current_col)


blockers = set()
with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for line in f:
        corners = re.findall(r"(\d+,\d+)", line)
        for i in range(0, len(corners) - 1):
            blockers.update(get_all_blockers(corners[i], corners[i + 1]))


step = 1
puzzle_1_blockers = blockers.copy()
sand = get_sand_puzzle_1(0, 500, blockers)

while sand:
    puzzle_1_blockers.add(sand)  # Sand will become the new blocker
    sand = get_sand_puzzle_1(0, 500, puzzle_1_blockers)
    step += 1

print(f"Puzzle 1: {step - 1}")

step = 1
puzzle_2_blockers = blockers.copy()
max_row = max([row for row, col in blockers]) + 1
sand = get_sand_puzzle_2(0, 500, puzzle_2_blockers, max_row)
while sand != (0, 500):
    puzzle_2_blockers.add(sand)  # Sand will become the new blocker
    sand = get_sand_puzzle_2(0, 500, puzzle_2_blockers, max_row)
    step += 1

print(f"Puzzle 2: {step}")
