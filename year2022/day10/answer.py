import os
import re

cycle = 0
ans = 0
x = 1


def cycle_check(cycle) -> bool:
    return (cycle - 20) % 40 == 0


def signal_strength(cycle, x) -> int:
    return cycle * x


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for line in [x.strip() for x in f.readlines()]:
        command, increment = re.match("(\w+) ?(-?\d+)?", line).groups()

        match command:
            case "noop":
                cycle += 1
                ans += signal_strength(cycle, x) if cycle_check(cycle) else 0
            case "addx":
                for _ in range(0, 2):
                    cycle += 1
                    ans += signal_strength(cycle, x) if cycle_check(cycle) else 0
                x += int(increment)
            case _:
                raise Exception("Unknown command")

print(f"Puzzle 1: {ans}")
