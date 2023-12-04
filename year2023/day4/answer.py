import os
import re

points = 0

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    lines = f.readlines()
    cards = [1 for _ in range(0, len(lines))]
    pattern = r"Card +(\d+): ([\d ]+) \| ([\d ]+)"
    for line in lines:
        card, winning, hand = re.match(pattern, line.strip()).groups()

        card = int(card)
        winning = re.findall(r"(\d+)", winning)
        hand = re.findall(r"(\d+)", hand)

        match_count = len([x for x in hand if x in winning])
        for shift in range(0, match_count):
            if card + shift < len(cards):
                cards[card + shift] += cards[card - 1]

        match match_count:
            case 0:
                pass
            case 1:
                points += 1
            case _:
                points += 2 ** (match_count - 1)

print(f'Puzzle 1: {points}')
print(f'Puzzle 2: {sum(cards)}')