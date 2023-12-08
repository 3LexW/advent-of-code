import os
from typing import List

ans = [0, 0, 0]
current = 0


def get_top_x(arr: List, new: int, top: int):
    arr = arr.copy()
    arr.append(new)
    arr.sort(reverse=True)
    return arr[0 : top]


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for line in f:
        if len(line.strip()) == 0:
            ans = get_top_x(ans, current, 3)
            current = 0
        else:
            current += int(line)

ans = get_top_x(ans, current, 3)
print(sum(ans))