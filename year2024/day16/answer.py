import os
from typing import List, Tuple
from math import inf
import heapq


class Map:
    graph: List[List[str]]
    starting_point: Tuple[int, int]
    ending_point: Tuple[int, int]
    ending_state: Tuple[int, int, int] = (None, None, None)

    queue = []  # (score, row, col, facing)
    lowest_score = {}
    backtrack = {}
    valid_backtrace_paths = []

    def __init__(self, graph):
        self.graph = graph
        self.starting_point = self._get_point("S")
        self.ending_point = self._get_point("E")

        self.queue.append(
            (0, self.starting_point[0], self.starting_point[1], 0, None, None, None)
        )
        self._dijkstra()

        self.queue.append(self.ending_state)
        self._trace()

    def _get_point(self, target: str):
        row = [i for i, row in enumerate(self.graph) if target in row][0]
        col = self.graph[row].index(target)
        return row, col

    def _dijkstra(self):
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

        while len(self.queue) > 0:
            (score, row, col, facing, last_row, last_col, last_facing) = heapq.heappop(
                self.queue
            )

            if self.graph[row][col] == "#":
                continue  # Out of bound

            if score > self.lowest_score.get((row, col, facing), inf):
                continue  # Not optimal

            if score < self.lowest_score.get((row, col, facing), inf):
                self.lowest_score[(row, col, facing)] = score
                self.backtrack[(row, col, facing)] = set()
            self.backtrack[(row, col, facing)].add((last_row, last_col, last_facing))

            if (row, col) == self.ending_point:
                if score < self.lowest_score.get(self.ending_state, inf):
                    self.ending_state = (row, col, facing)

            # go straight
            shift_row, shift_col = directions[facing]
            heapq.heappush(
                self.queue,
                (score + 1, row + shift_row, col + shift_col, facing, row, col, facing),
            )

            # left 90
            shift_row, shift_col = directions[(facing - 1) % 4]
            heapq.heappush(
                self.queue,
                (
                    score + 1001,
                    row + shift_row,
                    col + shift_col,
                    (facing - 1) % 4,
                    row,
                    col,
                    facing,
                ),
            )

            # right 90
            shift_row, shift_col = directions[(facing + 1) % 4]
            heapq.heappush(
                self.queue,
                (
                    score + 1001,
                    row + shift_row,
                    col + shift_col,
                    (facing + 1) % 4,
                    row,
                    col,
                    facing,
                ),
            )

    def _trace(self):
        while len(self.queue) > 0:
            current_node = self.queue.pop(0)
            if current_node in self.valid_backtrace_paths or current_node == (
                None,
                None,
                None,
            ):
                continue

            self.valid_backtrace_paths.append(current_node)
            for node in self.backtrack[current_node]:
                self.queue.append(node)


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    map = Map([list(x.strip()) for x in f.readlines()])
    print(
        f"Puzzle 1: {[score for (row, col, _), score in map.lowest_score.items() if (row, col) == map.ending_point][0]}"
    )
    print(f"PUzzle 2: {len(set((r, c) for (r, c, _) in map.valid_backtrace_paths))}")
