import os

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    inputs = [int(x.strip()) for x in f.readlines()]

print(f'Part 1: {sum([1 for i, num in enumerate(inputs) if i > 0 and inputs[i] > inputs[i-1]])}')

puzzle2 = [sum(inputs[i-2:i+1]) for i, num in enumerate(inputs) if i > 1]
print(f'Part 2: {sum([1 for i, num in enumerate(puzzle2) if i > 0 and puzzle2[i] > puzzle2[i-1]])}')
