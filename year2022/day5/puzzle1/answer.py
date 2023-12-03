import os
import re
from typing import List

import re
from typing import List

def get_initial_state(lines: List[str]) -> List[List[str]]:
    pattern = re.compile(r"\d+")
    stack_cnt = pattern.findall(lines[-1])
    stacks = [[] for n in stack_cnt]

    for line in lines[0:-1]:
        pointer = 0
        stack = 0
        for i in range(0, len(stack_cnt)):
            input = line[pointer + 1: pointer + 2]
            if len(input.strip()) > 0: stacks[stack].append(input) 
            stack += 1
            pointer += 4

    return stacks


def move_stack(stack: List[List[str]], count: int, from_stack: int, to_stack: int):
    for _ in range(0, count):
        item = stack[from_stack - 1].pop(0)
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
