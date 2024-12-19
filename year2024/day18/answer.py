import os
import re
from typing import List, Tuple


class Graph:
    width: int
    height: int
    corrupted: List[Tuple[int, int]]

    def __init__(self, width, height, corrupted):
        self.width = width
        self.height = height
        self.corrupted = corrupted

    def bfs(self):
        result = {}  # pos: step
        stack = []

        stack.append((0, 0, 0))  # pos_x, pos_y, step
        while len(stack) > 0:
            pos_x, pos_y, step = stack.pop(0)

            if (pos_x, pos_y) in result.keys():
                continue  # Visited position no need to search again
            if (pos_x, pos_y) in self.corrupted:
                continue  # Corrupted position cannot be travelled
            if not (0 <= pos_x <= self.width and 0 <= pos_y <= self.height):
                continue  # Out of bound

            if pos_x == self.width and pos_y == self.height:
                return step  # Reach the target location

            result[(pos_x, pos_y)] = step  # Minimum steps

            for shift_x, shift_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                stack.append((pos_x + shift_x, pos_y + shift_y, step + 1))


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    data = [re.findall(r"(\d+),(\d+)", x.strip())[0] for x in f.readlines()]
    corrupted = [(tuple(map(int, x))) for x in data]

graph1 = Graph(70, 70, corrupted[:1024])
print(f"Puzzle 1: {graph1.bfs()}")

for i in range(len(corrupted), 1024, -1):  # End with 1024 since it works in graph1
    print(i, end="\r")
    graph2 = Graph(70, 70, corrupted[:i])
    result = graph2.bfs()
    if result is not None:
        print(f"Puzzle 2: {corrupted[i]}")
        exit()
