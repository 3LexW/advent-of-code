import os
import re

value = {}
assignments = []

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for line in [x.strip() for x in f.readlines()]:
        if ":" in line:
            value[line.split(": ")[0]] = int(line.split(": ")[1]) == 1
        if "->" in line:
            a, operator, b, to_value = re.findall(
                r"(.*) (OR|AND|XOR) (.*) -> (.*)", line
            )[0]
            assignments.append((a, operator, b, to_value))

while assignments:
    a, operator, b, to_value = assignments.pop(0)
    if (a in value and b in value) is False:
        assignments.append((a, operator, b, to_value))
        continue
    match operator:
        case "OR":
            value[to_value] = value[a] or value[b]
        case "XOR":
            value[to_value] = value[a] != value[b]
        case "AND":
            value[to_value] = value[a] and value[b]

p1 = 0
for key, b in sorted({key: value for key, value in value.items() if key.startswith("z")}.items(), reverse=True):
    p1 = p1 << 1
    p1 += int(b)

print(f"Puzzle 1: {p1}")