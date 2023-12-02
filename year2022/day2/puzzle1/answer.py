import os

ans = 0
outcome = {
    'A X': 3,
    'B Y': 3,
    'C Z': 3,
    'A Y': 6,
    'B Z': 6,
    'C X': 6,
    'A Z': 0,
    'B X': 0,
    'C Y': 0
}
shape = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    print(sum([
        outcome[x.strip()] + shape[x.strip().split(' ')[-1]]
        for x 
        in f.readlines()]))