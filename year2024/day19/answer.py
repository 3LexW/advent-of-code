import os
from functools import lru_cache

@lru_cache(maxsize=None)
def possible_combo(target: str, patterns: str):
    if len(target) == 0:
        return 1
    
    ans = 0
    for pattern in patterns.split(","):
        if target.startswith(pattern):
            ans += possible_combo(target.removeprefix(pattern), patterns)
    return ans


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    available = ",".join(f.readline().strip().split(", "))
    desire_patterns = [x.strip() for x in f.readlines() if len(x.strip()) > 0]


p1 = 0
p2 = 0

for desire_pattern in desire_patterns:
    combos = possible_combo(desire_pattern, available)
    if combos > 0:
        p1 += 1
    p2 += combos

print(f"Puzzle 1: {p1}")
print(f"Puzzle 1: {p2}")
