import os
import re

cycle = 0
ans = 0
x = 1

crt = ""


def cycle_check(cycle) -> bool:
    return (cycle - 20) % 40 == 0


def signal_strength(cycle, x) -> int:
    return cycle * x


def get_next_crt(cycle, x) -> str:
    # Draw based on current cycle position
    return "#" if x - 1 <= (cycle - 1) % 40 <= x + 1 else "."


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for line in [x.strip() for x in f.readlines()]:
        command, increment = re.match("(\w+) ?(-?\d+)?", line).groups()

        match command:
            case "noop":
                crt += get_next_crt(cycle + 1, x)
                cycle += 1
                ans += signal_strength(cycle, x) if cycle_check(cycle) else 0
            case "addx":
                for _ in range(0, 2):
                    crt += get_next_crt(cycle + 1, x)
                    cycle += 1
                    ans += signal_strength(cycle, x) if cycle_check(cycle) else 0
                x += int(increment)
            case _:
                raise Exception("Unknown command")


print(f"Puzzle 1: {ans}")
print(f"Puzzle 2: ")
for i in range(0, len(crt), 40):
    print(crt[i : i + 40])
