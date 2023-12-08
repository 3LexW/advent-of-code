from ast import List
import os
from typing import Optional, Union
import ast


class Pair:
    left: []
    right: []
    valid_pair: bool

    def __init__(self, left: [], right: []) -> None:
        self.left = left
        self.right = right
        self.valid_pair = self.check_valid_pair(self.left, self.right)

    def is_valid_pair_int(self, left: int, right: int) -> Optional[bool]:
        if left == right:
            return None
        else:
            return left < right

    def check_valid_pair(self, left: Union[int, List], right: Union[int, List]) -> bool:
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


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    lines = [x.strip() for x in f.readlines() if len(x.strip()) > 0]

pairs = []
for i in range(0, len(lines), 2):
    pairs.append(Pair(ast.literal_eval(lines[i]), ast.literal_eval(lines[i + 1])))

scores = [i + 1 for i, x in enumerate(pairs) if x.valid_pair]
print(f"Puzzle 1: {sum(scores)}")
