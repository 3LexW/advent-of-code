import os
import sys
sys.path.append(os.getcwd())
from day2.shared import split_line

ans = 0
with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    lines = f.readlines()


def violation_check(draw: str):
    maximums = {"red": 12, "green": 13, "blue": 14}
    # draw should be in format 'number color'
    split = draw.split(' ')
    try:
        number = int(split[0])
        color = split[1]
        if color not in maximums.keys():
            print(f"Unknown color: {color}")
            raise Exception("Unknown color")
        return number > maximums[color]

    except:
        print(f"Exception: Violation on line {draw}")


for line in lines:
    game_id, draws = split_line(line)
    violation = [draw for draw in draws if violation_check(draw) == True]
    if len(violation) == 0:
        ans += game_id

print(ans)