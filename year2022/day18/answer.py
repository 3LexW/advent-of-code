import os
import re
import itertools

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    lines = [list(map(int, re.findall(r"(\d+)", line))) for line in lines]

visited = set()

shifts = [
    shift
    for shift in list(itertools.product(*[[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]))
    if shift.count(0) == 2
]

ans = 0
for x, y, z in lines:
    ans += 6
    for x_shift, y_shift, z_shift in shifts:
        if (x + x_shift, y + y_shift, z + z_shift) in visited:
            ans -= 2
    visited.add((x, y, z))

print(f"Puzzle 1: {ans}")

p2_ans = 0

max_x = max(line[0] for line in lines)
max_y = max(line[1] for line in lines)
max_z = max(line[2] for line in lines)

safe = set()
not_safe = set()


def trapped(x, y, z):
    global visited, safe, shifts, max_x, max_y, max_z
    stack = [(x, y, z)]
    self_visited = set()
    while stack:
        x_cur, y_cur, z_cur = stack.pop()
        self_visited.add((x_cur, y_cur, z_cur))
        for x_shift, y_shift, z_shift in shifts:
            next_loc = (x_cur + x_shift, y_cur + y_shift, z_cur + z_shift)
            if next_loc in visited or next_loc in self_visited:
                continue  # Blocked
            if next_loc in safe:
                return False  # Early escape, if it reach safe position, it must be safe
            if next_loc in not_safe:
                return True  # Early escape, if it reach non safe position, it must be trapped
            if (
                not 0 < x_cur + x_shift <= max_x
                or not 0 < y_cur + y_shift <= max_y
                or not 0 < z_cur + z_shift <= max_z
            ):
                return False  # Not trapped, safe
            stack.append(next_loc)
    # If no way to go, trapped
    return True


cnt = 0
for x in range(1, max_x + 1):
    for y in range(1, max_y + 1):
        for z in range(1, max_z + 1):
            cnt += 1
            print(f"Checking block {cnt}/{max_x * max_y * max_z}", end="\r")
            if (x, y, z) in visited:
                continue  # It is the block, should not check
            if trapped(x, y, z):
                not_safe.add((x, y, z))
            else:
                safe.add((x, y, z))

# Calculate the surface area of the trapped air blocks
ans_trapped = 0
visited = set()
for x, y, z in not_safe:
    ans_trapped += 6
    for x_shift, y_shift, z_shift in shifts:
        if (x + x_shift, y + y_shift, z + z_shift) in visited:
            ans_trapped -= 2
    visited.add((x, y, z))

print()
print(f"Puzzle 2: {ans - ans_trapped}")
