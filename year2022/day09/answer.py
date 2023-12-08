import os
from typing import Dict, Set, Tuple

mapping = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}


def move_tail(head: Tuple[int, int], tail: Tuple[int, int]) -> Tuple[int, int]:
    difference = (head[0] - tail[0], head[1] - tail[1])
    shift_map: Dict[Tuple[int, int], Tuple[int, int]] = {
        (2, 1): (1, 1),
        (1, 2): (1, 1),
        (2, 0): (1, 0),
        (2, -1): (1, -1),
        (1, -2): (1, -1),
        (0, -2): (0, -1),
        (-1, -2): (-1, -1),
        (-2, -1): (-1, -1),
        (-2, 0): (-1, 0),
        (-2, 1): (-1, 1),
        (-1, 2): (-1, 1),
        (0, 2): (0, 1),
        (2, 2): (1, 1),
        (-2, -2): (-1, -1),
        (-2, 2): (-1, 1),
        (2, -2): (1, -1),
    }

    shift = shift_map.get(difference)
    return (tail[0] + shift[0], tail[1] + shift[1]) if shift else tail


def get_ans(tail_count: int) -> int:
    T_history: Set[Tuple[int, int]] = set([(0, 0)])

    # First knot is the head, and last knot is the tail
    knots = [(0, 0)] + [(0, 0) for _ in range(0, tail_count)]
    with open(f"{os.path.dirname(__file__)}/input.txt") as f:
        for line in f:
            direction, step = line.strip().split(" ")
            for _ in range(0, int(step)):
                knots[0] = (
                    knots[0][0] + mapping[direction][0],
                    knots[0][1] + mapping[direction][1],
                )
                for i in range(1, len(knots)):
                    knots[i] = move_tail(knots[i - 1], knots[i])
                T_history.add(knots[-1])

    return len(T_history)


print(f"Puzzle 1: {get_ans(1)}")
print(f"Puzzle 2: {get_ans(9)}")
