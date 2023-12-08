import os

ans = 0

"""
A: Rock, B: Paper, C:Scissors
X: Lose, Y: Draw, Z:Win
Rock: 1, Paper: 2, Scissors: 3
"""
outcome = {
    "A X": 0 + 3,
    "B Y": 3 + 2,
    "C Z": 6 + 1,
    "A Y": 3 + 1,
    "B Z": 6 + 3,
    "C X": 0 + 2,
    "A Z": 6 + 2,
    "B X": 0 + 1,
    "C Y": 3 + 3,
}

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    print(sum([outcome[x.strip()] for x in f.readlines()]))
