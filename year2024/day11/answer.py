from functools import lru_cache
import os


@lru_cache(maxsize=None)
def stone_action(stone: int, iteration: int):
    if iteration == 0:
        return 1  # Last blink

    if stone == 0:
        return stone_action(1, iteration - 1)
    if len(str(stone)) % 2 == 0:
        stone = str(stone)
        firstpart, secondpart = stone[: len(stone) // 2], stone[len(stone) // 2 :]
        return stone_action(int(firstpart), iteration - 1) + stone_action(
            int(secondpart), iteration - 1
        )
    return stone_action(stone * 2024, iteration - 1)


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    stones = list(map(int, f.readline().strip().split()))

p1 = 0
p2 = 0

for stone in stones:
    print(f"Processing stone: {stone}")
    p1 += stone_action(stone, 25)
    p2 += stone_action(stone, 75)


print(f"Puzzle 1: {p1}")
print(f"Puzzle 2: {p2}")
