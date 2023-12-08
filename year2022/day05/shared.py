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