import os
import re

p1_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
p2_ignore_pattern = r"don't\(\).*?do\(\)"
p2_ignore_pattern2 = r"don't\(\).*"
p1_matches = []
p2_matches = []

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    line = ''.join([x.strip() for x in f.readlines()])

    p1_matches.extend(re.findall(p1_pattern, line))

    # Ignore all between don't() and do()
    p2_update_string = re.sub(p2_ignore_pattern, '', line)
    p2_update_string = re.sub(p2_ignore_pattern2, '', p2_update_string)

    # Ignore all after don't() at the end of the string
    p2_matches.extend(re.findall(p1_pattern, p2_update_string))

print(f"Puzzle 1: {sum([int(a) * int(b) for a, b in p1_matches])}")
print(f"Puzzle 2: {sum([int(a) * int(b) for a, b in p2_matches])}")