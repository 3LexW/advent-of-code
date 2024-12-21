import os
from typing import Dict, List
from abc import ABC
from pprint import pp


class Pad(ABC):
    target_strings: List[str]
    movements = [
        ("^", -1, 0),
        (">", 0, 1),
        ("v", 1, 0),
        ("<", 0, -1),
    ]
    layout: List[List[str]]
    width: int
    height: int
    move_map = {}
    target_paths = []

    def __init__(self, target_string):
        self.target_strings = target_string
        self.height = len(self.layout)
        self.width = len(self.layout[0])
        self._set_move_map()
        self._get_paths()

    def _set_move_map(self):
        keys = [x for x in sum(self.layout, []) if x is not None]
        for i in range(0, len(keys)):
            if keys[i] not in self.move_map:
                self.move_map[keys[i]] = {}
            for j in range(0, len(keys)):
                self.move_map[keys[i]][keys[j]] = self._bfs(keys[i], keys[j])

    def _bfs(self, from_key, to_key):
        visited = {}
        stack = [(from_key, "")]

        while len(stack) > 0:
            current_key, moves = stack.pop(0)

            if current_key not in visited or len(moves) < len(visited[current_key][0]):
                visited[current_key] = [moves]
            elif len(moves) == len(visited[current_key][0]):
                visited[current_key].append(moves)
            else:
                continue

            current_row = [
                i for i, row in enumerate(self.layout) if current_key in row
            ][0]
            current_col = self.layout[current_row].index(current_key)

            for step, row_shift, col_shift in self.movements:
                new_row, new_col = current_row + row_shift, current_col + col_shift
                if not (0 <= new_row < self.height and 0 <= new_col < self.width):
                    continue
                if self.layout[new_row][new_col] is None:
                    continue
                stack.append((self.layout[new_row][new_col], moves + step))

        return visited[to_key]

    def _get_paths(self):
        possible_paths = []
        for target_string in self.target_strings:
            possible_paths.extend(self._get_path(target_string))
        min_length = len(min(possible_paths, key=lambda item: len(item)))
        current_step_path = [x for x in possible_paths if len(x) == min_length]
        self.target_paths = current_step_path

    def _get_path(self, target_string: str):
        current_key = "A"
        current_step_path = [""]
        for target_key in target_string:
            target_key_path = []
            for possible_path in self.move_map[current_key][target_key]:
                for current_step in current_step_path:
                    target_key_path.append(current_step + possible_path + "A")
            current_step_path = target_key_path.copy()
            current_key = target_key
        return current_step_path


class NumPad(Pad):
    def __init__(self, target_string):
        self.layout = [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            [None, "0", "A"],
        ]
        super().__init__(target_string)


class KeyPad(Pad):
    def __init__(self, target_string):
        self.layout = [[None, "^", "A"], ["<", "v", ">"]]
        super().__init__(target_string)


p1 = 0

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    goals = [x.strip() for x in f.readlines()]
    for goal in goals:
        numpad = NumPad([goal])
        target_paths = numpad.target_paths
        for i in range(2):
            keypad = KeyPad(target_paths)
            target_paths = keypad.target_paths
        shortest_len = len(keypad.target_paths[0])

        num_val = int(goal.replace("A", ""))
        p1 += num_val * shortest_len

print(f"Puzzle 1: {p1}")