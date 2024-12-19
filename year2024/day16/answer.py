import os
from typing import List, Tuple


class Map:
    graph: List[List[str]]
    starting_point: Tuple[int, int]
    ending_point: Tuple[int, int]

    def __init__(self, graph):
        self.graph = graph
        self.starting_point = self._get_point("S")
        self.ending_point = self._get_point("E")

    def _get_point(self, target: str):
        row = [i for i, row in enumerate(self.graph) if target in row][0]
        col = self.graph[row].index(target)
        return row, col

    def dijkstra(self):
        visited = {}
        scores = {}
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

        def add_to_queue(row, col, facing, score):
            scores[(row, col, facing)] = score

        def pop_from_queue():
            entry = min(scores.items(), key=lambda item: item[1])
            scores.pop(entry[0])
            return entry[0], entry[1]

        add_to_queue(self.starting_point[0], self.starting_point[1], 0, 0)
        while len(scores) > 0:
            (row, col, facing), score = pop_from_queue()

            if (row, col, facing) in visited:
                continue  # The point is already optimized

            if self.graph[row][col] == "#":
                continue  # Out of bound

            if (row, col) == self.ending_point:
                return score

            visited[(row, col, facing)] = score

            # go straight
            shift_row, shift_col = directions[facing]
            add_to_queue(row + shift_row, col + shift_col, facing, score + 1)

            # left 90
            shift_row, shift_col = directions[(facing - 1) % 4]
            add_to_queue(
                row + shift_row, col + shift_col, (facing - 1) % 4, score + 1001
            )

            # right 90
            shift_row, shift_col = directions[(facing + 1) % 4]
            add_to_queue(
                row + shift_row, col + shift_col, (facing + 1) % 4, score + 1001
            )


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    map = Map([list(x.strip()) for x in f.readlines()])
    print(f"Puzzle 1: {map.dijkstra()}")
