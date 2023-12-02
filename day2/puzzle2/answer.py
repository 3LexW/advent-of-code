from functools import reduce
import os
import sys
sys.path.append(os.getcwd())
from day2.shared import split_line
from typing import Dict

ans = 0
with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    lines = f.readlines()

def max_for_each_color(acc: Dict[str, int], ele: str):
    if acc == None:
        acc = {}

    split = ele.split(' ')
    try:
        number = int(split[0])
        color = split[1]
    except:
        print(f"Exception: Violation on line {ele}")

    if color not in acc.keys():
        acc[color] = 0
    acc[color] = max(acc[color], number) 

    return acc


for line in lines:
    _, draws = split_line(line)
    min_req = reduce(max_for_each_color, draws, None)
    power = reduce(lambda a, b: a*b, min_req.values())
    ans += power

print(ans)