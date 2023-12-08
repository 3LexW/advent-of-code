import os


def get_marker(length: int):
    with open(f"{os.path.dirname(__file__)}/input.txt") as f:
        pointer = length
        s = f.read(length)
        while len(set([char for char in s])) != length:
            pointer += 1
            s = s[1:] + f.read(1)
    return pointer


print(f"Puzzle 1: {get_marker(4)}")
print(f"Puzzle 1: {get_marker(14)}")
