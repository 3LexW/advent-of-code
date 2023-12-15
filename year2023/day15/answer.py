import copy
import os
import re
from typing import List, Tuple
from pprint import pp


def hash(s: str) -> int:
    ans = 0
    for c in s:
        ans += ord(c)
        ans *= 17
        ans %= 256
    return ans


def place_lens(boxes: List[List[Tuple[str, int]]], label, lens, operation):
    box_index = hash(label)
    item_index = -1
    for i in range(len(boxes[box_index])):
        if boxes[box_index][i][0] == label:
            item_index = i

    match operation:
        case "-":
            if item_index >= 0:
                boxes[box_index].pop(item_index)
        case "=":
            if item_index >= 0:
                boxes[box_index][item_index] = (label, lens)
            else:
                boxes[box_index].append((label, lens))

    return boxes


def puzzle2(boxes: List[List[Tuple[str, int]]]) -> int:
    ans = 0
    for box_id in range(len(boxes)):
        for slot_id in range(len(boxes[box_id])):
            _, lens = boxes[box_id][slot_id]
            ans += (box_id + 1) * (slot_id + 1) * int(lens)
    return ans


boxes = [[] for _ in range(256)]

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    words = f.readline().strip().split(",")

    ans = 0
    for word in words:
        ans += hash(word)

        label, operation, lens = re.match(r"(\w+)([-=])(\d?)", word).groups()
        boxes = place_lens(copy.deepcopy(boxes), label, lens, operation)


print(f"Puzzle 1: {ans}")
print(f"Puzzle 2: {puzzle2(boxes)}")
