import os
import re
from sympy import symbols, Eq, solve

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    data = "\n".join([x.strip() for x in f.readlines()])

pattern = re.compile(
    r"Button A: X\+(\d+), Y\+(\d+)\s+"  # Match Button A values (ax, ay)
    r"Button B: X\+(\d+), Y\+(\d+)\s+"  # Match Button B values (bx, by)
    r"Prize: X=(\d+), Y=(\d+)"  # Match Prize values (goal_x, goal_y)
)
p1 = 0
p2 = 0

# Find all matches
matches = pattern.findall(data)

# Process and display the results
for match in matches:
    ax, ay, bx, by, goal_x, goal_y = map(int, match)
    a, b = symbols("a,b", integer=True)

    eq1 = Eq(ax * a + bx * b, goal_x)
    eq2 = Eq(ay * a + by * b, goal_y)

    solution = solve((eq1, eq2), (a, b))
    if solution:
        p1 += 3 * solution[a] + solution[b]

    eq1 = Eq(ax * a + bx * b, goal_x + 10000000000000)
    eq2 = Eq(ay * a + by * b, goal_y + 10000000000000)
    solution = solve((eq1, eq2), (a, b))
    if solution:
        p2 += 3 * solution[a] + solution[b]

print(f"Puzzle 1: {p1}")
print(f"Puzzle 1: {p2}")
