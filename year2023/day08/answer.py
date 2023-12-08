from math import lcm
import os, re


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    lines = f.readlines()

required_steps = lines[0].strip()
nodes = lines[2:]

node_list = [line[0:3] for line in nodes]
lefts = [line[7:10] for line in nodes]
rights = [line[12:15] for line in nodes]

step_cnt = 0
step_index = 0

current_index = node_list.index("AAA")
while node_list[current_index] != "ZZZ":
    match required_steps[step_index]:
        case "L":
            current_index = node_list.index(lefts[current_index])
        case "R":
            current_index = node_list.index(rights[current_index])
    step_cnt += 1
    step_index = 0 if step_index == len(required_steps) - 1 else step_index + 1

print(f"Puzzle 1: {step_cnt}")


# Part 2

current_indexes = [i for i, x in enumerate(node_list) if x.endswith("A")]
result = []


for i in current_indexes:
    current_index = i
    step_cnt = 0
    step_index = 0

    while node_list[current_index].endswith("Z") == False:
        match required_steps[step_index]:
            case "L":
                current_index = node_list.index(lefts[current_index])
            case "R":
                current_index = node_list.index(rights[current_index])
        step_cnt += 1
        step_index = 0 if step_index == len(required_steps) - 1 else step_index + 1
    result.append(step_cnt)

print(f"Puzzle 2: {lcm(*result)}")
