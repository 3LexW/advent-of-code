import os
from typing import Set, Tuple

# Set beginning position
H = (0, 0)
T = (0, 0)

T_history: Set[Tuple[int, int]] = set([T])
H_previous_step = (0, 0)

mapping = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for line in f:
        direction, step = line.strip().split(' ')
        for _ in range(0, int(step)):
            H_previous_step = H
            H = (H[0] + mapping[direction][0], H[1] + mapping[direction][1])
            if abs(T[0] - H[0]) >= 2 or abs(T[1] - H[1]) >= 2:
                T = H_previous_step
                T_history.add(T)

print(f"Puzzle 1: {len(T_history)}")