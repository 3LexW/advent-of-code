from math import ceil, floor, sqrt, prod
import os
import re


def get_result(time, distance):
    """
    Use quadratic equation
    > (t-x) * x= d
    > tx-x^2 = d
    > -x^2+tx-d = 0
    > x = -t(+-)sqrt(t^2-4d) / -2

    lower = max(0, round up lower x)
    higher = min(time, round down upper x)
    """

    x_up = (-time + sqrt(time**2 - 4 * distance)) / -2
    x_down = (-time - sqrt(time**2 - 4 * distance)) / -2

    # Going further is required, so equal does not count
    if x_up.is_integer():
        x_up += 1
    if x_down.is_integer():
        x_down -= 1

    lower = max(0, ceil(x_up))
    higher = min(time, floor(x_down))

    return higher - lower + 1


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    times = re.findall(r"(\d+)", f.readline())
    distances = re.findall(r"(\d+)", f.readline())

print(f"Puzzle 1: {prod([get_result(int(t), int(d)) for t,d in zip(times, distances)])}")

# Part 2
t, d = int("".join(times)), int("".join(distances))
print(f"Puzzle 2: {get_result(int(t), int(d))}")
