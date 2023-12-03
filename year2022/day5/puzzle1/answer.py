import os
import sys

sys.path.append(os.getcwd())
import re
from typing import List
from year2022.day5.shared import get_initial_state


def move_stack(stack: List[List[str]], count: int, from_stack: int, to_stack: int) -> List[List[str]]:
    for _ in range(0, count):
        item = stack[from_stack - 1].remove()
        stack[to_stack - 1].insert(0, item)
    return stack


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    # Get initial stack
    lines = []
    line = f.readline()
    while line.strip() != "":
        lines.append(line)
        line = f.readline()
    state = get_initial_state(lines)

    line = f.readline()
    while line.strip() != "":
        match = re.match(r"move (\d+) from (\d+) to (\d+)", line)
        if match:
            count = int(match.group(1))
            from_stack = int(match.group(2))
            to_stack = int(match.group(3))
            state = move_stack(state, count, from_stack, to_stack)
        line = f.readline()

    print("".join([x[0] for x in state]))
