import os
import re

ans = 0

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for line in f:
        # Input format: A-B,C-D
        a, b, c, d = re.split("[-,]", line.strip())
        a, b, c, d = int(a), int(b), int(c), int(d)
        if (a <= c <= d <= b) or (c <= a <= b <= d):
            ans += 1

print(ans)
