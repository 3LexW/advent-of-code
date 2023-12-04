import os
import re

points = 0

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    pattern = r"Card.*(\d+): ([\d ]+) \| ([\d ]+)"
    for line in f:
        card, winning, hand = re.match(pattern, line.strip()).groups()
        winning = re.findall(r"(\d+)", winning)
        hand = re.findall(r"(\d+)", hand)

        match_count = len([x for x in hand if x in winning])
        match match_count:
            case 0:
                pass
            case 1:
                points += 1
            case _:
                points += 2 ** (match_count - 1)

print(f'Puzzle 1: {points}')