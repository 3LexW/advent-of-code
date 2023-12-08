from ast import List
import os
from typing import Optional, Union
import ast


class Input:
    input: []

    def __init__(self, input: []) -> None:
        self.input = input

    def is_valid_pair_int(self, left: int, right: int) -> Optional[bool]:
        if left == right:
            return None
        else:
            return left < right

    def check_valid_pair(self, left: Union[int, List], right: Union[int, List]) -> bool:
        """Check if left input is smaller than right input"""
        for i in range(0, len(left)):
            if i >= len(right):
                return False  # Right side run out of items
            l = left[i]
            r = right[i]

            if isinstance(l, int) and isinstance(r, int):
                result = self.is_valid_pair_int(l, r)
                if result is not None:
                    return result
            else:
                if isinstance(l, list) == False:
                    l = [l]
                if isinstance(r, list) == False:
                    r = [r]

                result = self.check_valid_pair(l, r)
                if result is not None:
                    return result

        # Left run out of items
        if len(left) < len(right):
            return True

        # Two share the same result
        return None

    def __lt__(self, other):
        return self.check_valid_pair(self.input, other.input)


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    inputs = [
        Input(ast.literal_eval(x.strip())) for x in f.readlines() if len(x.strip()) > 0
    ]

pairs = []
for i in range(0, len(inputs), 2):
    pairs.append([inputs[i], inputs[i + 1]])

score = 0
for i, pair in enumerate(pairs):
    if pair[0] < pair[1]:
        score += i + 1


print(f"Puzzle 1: {score}")

divider1, divider2 = Input([[2]]), Input([[6]])
inputs.append(divider1)
inputs.append(divider2)

inputs.sort()

score = (inputs.index(divider1) + 1) * (inputs.index(divider2) + 1)
print(f"Puzzle 2: {score}")
