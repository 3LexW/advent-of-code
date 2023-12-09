import os, re
from typing import List


def get_next_layer(layer: List[int]) -> List[int]:
    ans = []
    for i in range(0, len(layer) - 1):
        ans.append(layer[i + 1] - layer[i])
    return ans


def get_next_end_value(current_layer: List[int], upper_layer: List[int]) -> int:
    if len(current_layer) != len(upper_layer):
        raise Exception(
            "Upper layer should has same number of values to the current layer"
        )
    return upper_layer[-1] + current_layer[-1]

def get_next_first_value(current_layer: List[int], upper_layer: List[int]) -> int:
    if len(current_layer) != len(upper_layer):
        raise Exception(
            "Upper layer should has same number of values to the current layer"
        )
    return upper_layer[0] - current_layer[0]


puzzle1_ans = 0
puzzle2_ans = 0

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for line in f:
        layers = [list(map(int, re.findall(r"(-?\d+)", line)))]
        while sum(layers[-1]) != 0:
            layers.append(get_next_layer(layers[-1]))

        layers[-1].append(0)
        for i in range(1, len(layers)):
            layers[-i - 1].append(get_next_end_value(layers[-i], layers[-i - 1]))

        layers[-1].append(0)
        for i in range(1, len(layers)):
            layers[-i - 1].insert(0, get_next_first_value(layers[-i], layers[-i - 1]))
    
        puzzle1_ans += layers[0][-1]
        puzzle2_ans += layers[0][0]

print(f"Puzzle 1: {puzzle1_ans}")
print(f"Puzzle 2: {puzzle2_ans}")

