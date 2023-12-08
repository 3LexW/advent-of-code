import os


ans = 0
current = 0

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for line in f:
        if len(line.strip()) == 0:
            ans = max(ans, current)
            current = 0
        else:
            current += int(line)

ans = max(ans, current)
print(ans)