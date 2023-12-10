import os
from typing import List, Set, Tuple
from pprint import pp

# All shifts are in (row, col)
shifts = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

connections = {"north": (-1, 0), "south": (1, 0), "east": (0, 1), "west": (0, -1)}

mapping = {
    "|": [connections["north"], connections["south"]],
    "-": [connections["east"], connections["west"]],
    "L": [connections["north"], connections["east"]],
    "J": [connections["north"], connections["west"]],
    "7": [connections["south"], connections["west"]],
    "F": [connections["south"], connections["east"]],
    "S": []
}


def get_connected_cells(row: int, col: int, value: str) -> List[Tuple[int, int]]:
    return [(row + r_shift, col + c_shift) for r_shift, c_shift in mapping[value]]


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    grid = [x.strip() for x in f.readlines()]

starting_row = max([i for i, x in enumerate(grid) if "S" in x])
starting_col = grid[starting_row].index("S")

# item structure ((row, col), (from_row, from_col), value, step_from_S)
stack: List[Tuple[Tuple[int, int], Tuple[int, int], str, int]] = []
loop: Set[Tuple[int, int]] = set()

# Determine the starting loop connections
for r_shift, c_shift in shifts:
    r_check, c_check = starting_row + r_shift, starting_col + c_shift
    check_value = grid[r_check][c_check]
    loop.add((starting_row, starting_col))
    if 0 <= r_check < len(grid) and 0 <= c_check < len(grid[0]) is False:
        continue  # Out of bound
    if (check_value in mapping.keys()) and (
        (
            starting_row,
            starting_col,
        )
        in get_connected_cells(r_check, c_check, check_value)
    ):
        stack.append(((r_check, c_check), (starting_row, starting_col), check_value, 1))

# Follow the loop
while len(stack) == 2:
    a, b = stack.pop(), stack.pop()
    loop.add(a[0])
    loop.add(b[0])
    if a[0] == b[0]:
        # Reach the end point
        print(f"Puzzle 1: {a[-1]}")
        break

    for node in [a, b]:
        (row, col), from_node, value, step_from_S = node
        next_pos = [x for x in get_connected_cells(row, col, value) if from_node != x][
            0
        ]
        next_value = grid[next_pos[0]][next_pos[1]]
        stack.append((next_pos, (row, col), next_value, step_from_S + 1))

# Draw an updated grid
grid2 = []
for r in range(0, len(grid)):
    row = ''
    for c in range(0, len(grid[0])):
        row += '.' if (r, c) not in loop else grid[r][c]
    grid2.append(row)
 
# Draw the grid in 2x coordinate
double_grid: List[str] = []
for row in grid:
    double_grid.append([".", "."] * len(row))
    double_grid.append([".", "."] * len(row))


for row, col in loop:
    double_grid[row * 2][col * 2] = grid[row][col]

for row, col in loop:
    for r_shift, c_shift in mapping[grid[row][col]]:
        if double_grid[row * 2 + r_shift][col * 2 + c_shift] == '.':
            double_grid[row * 2 + r_shift][col * 2 + c_shift] = '-' if r_shift == 0 else '|'

double_grid = ["".join(row) for row in double_grid]

# pp(grid2)
# pp(double_grid)


def is_trapped(grid: List[str], row: int, col: int) -> bool:
    visited = set()
    stack = [(row, col)]
    while stack:
        r, c = stack.pop()
        for r_shift, c_shift in shifts:
            if (
                0 <= r + r_shift < len(grid) and 0 <= c + c_shift < len(grid[0])
            ) == False:
                return False  # Out of bound, not trapped
            if (
                grid[r + r_shift][c + c_shift] != "."
                or (r + r_shift, c + c_shift) in visited
            ):
                continue
            stack.append((r + r_shift, c + c_shift))
        visited.add((r, c))
    return True


puzzle2_ans = 0
for r in range(0, len(grid2)):
    for c in range(0, len(grid2[r])):
        if (
            (r, c) not in loop
            and is_trapped(grid2, r, c)
            and is_trapped(double_grid, r * 2, c * 2)
        ):
            puzzle2_ans += 1

print(f"Puzzle 2: {puzzle2_ans}")
