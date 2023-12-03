import os
import sys
import re
from typing import List

sys.path.append(os.getcwd())
from year2022.day5.shared import get_initial_state


def move_stack(
    state: List[List[str]], count: int, from_stack: int, to_stack: int
) -> List[List[str]]:
    items: List[str] = []
    for _ in range(0, count):
        items.append(state[from_stack - 1].pop(0))
    state[to_stack - 1] = items + state[to_stack - 1]
    return state


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
