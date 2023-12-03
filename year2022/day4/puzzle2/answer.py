import os
import re

ans = 0

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for line in f:
        a, b, c, d = [int(x) for x in re.split('[,-]', line)]
        if c <= a <= d or a <= c <= b:
            ans += 1

print(ans)