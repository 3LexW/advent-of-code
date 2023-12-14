import os
from typing import List


def is_mirror(left: List[str], right: List[str]) -> bool:
    """Check from last item for left, and check from first item for right, see if identical"""
    for i in range(0, min(len(left), len(right))):
        if left[len(left) - 1 - i] != right[i]:
            return False
    return True


def is_smudge(left: List[str], right: List[str]) -> bool:
    """Check from last item for left, and check from first item for right, see if having only 1 difference"""
    diff = 0
    for i in range(0, min(len(left), len(right))):
        diff += sum(
            [
                1
                for c in range(len(left[len(left) - 1 - i]))
                if left[len(left) - 1 - i][c] != right[i][c]
            ]
        )
    return diff == 1


def check_horizontal_flip_row(puzzle: List[str]) -> int:
    for i in range(0, len(puzzle) - 1):
        if is_mirror(puzzle[0 : i + 1], puzzle[i + 1 :]):
            return i + 1
    return 0


def check_smudge_row(puzzle: List[str]) -> int:
    for i in range(0, len(puzzle) - 1):
        if is_smudge(puzzle[0 : i + 1], puzzle[i + 1 :]):
            return i + 1
    return 0


def check_vertical_flip(puzzle: List[str]) -> int:
    return check_horizontal_flip_row(flip_puzzle(puzzle))


def flip_puzzle(puzzle: List[str]) -> List[str]:
    # Flip the puzzle
    p = []
    for i in range(len(puzzle[0])):
        p.append("".join([l[i] for l in puzzle]))
    return p


def get_puzzle1(puzzle: List[str]):
    return 100 * check_horizontal_flip_row(puzzle) + check_vertical_flip(puzzle)


def get_puzzle2(puzzle: List[str]):
    return 100 * check_smudge_row(puzzle) + check_smudge_row(flip_puzzle(puzzle))


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

    result1 = 0
    result2 = 0

    start = 0
    for i in range(0, len(lines)):
        if len(lines[i]) == 0:
            result1 += get_puzzle1(lines[start:i])
            result2 += get_puzzle2(lines[start:i])
            start = i + 1

    result1 += get_puzzle1(lines[start:])
    result2 += get_puzzle2(lines[start:])

print(f"Puzzle 1: {result1}")
print(f"Puzzle 2: {result2}")
