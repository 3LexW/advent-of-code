import os
from pprint import pp
from typing import List, Tuple


class Warehouse:
    map: List[List[str]]
    command: List[str]
    command_pointer: int
    robot_pos: Tuple[int, int]

    def __init__(self, map, command):
        self.map = map
        self.command = command
        robot_row = [i for i, x in enumerate(self.map) if "@" in x][0]
        robot_col = [j for j, row in enumerate(self.map[robot_row]) if "@" in row][0]
        self.robot_pos = (robot_row, robot_col)
        self.command_pointer = 0

    def _get_move(self):
        match self.command[self.command_pointer]:
            case "^":
                move_row, move_col = (-1, 0)
            case "<":
                move_row, move_col = (0, -1)
            case ">":
                move_row, move_col = (0, 1)
            case "v":
                move_row, move_col = (1, 0)
            case _:
                raise ValueError(
                    f"{self.command[self.command_pointer]} is not a valid command (pos {self.command_pointer})"
                )
        return move_row, move_col

    def execute_move(self):
        robot_row, robot_col = self.robot_pos
        move_row, move_col = self._get_move()
        shift = 1
        while self.map[robot_row + move_row * shift][
            robot_col + move_col * shift
        ] not in (".", "#"):
            shift += 1
        if self.map[robot_row + move_row * shift][robot_col + move_col * shift] == ".":
            # Move all the items
            for i in range(0, shift):
                self.map[robot_row + move_row * (shift - i)][robot_col + move_col * (shift - i)] = self.map[robot_row + move_row * (shift - i - 1)][robot_col + move_col * (shift - i - 1)]
            self.map[robot_row][robot_col] = "."
            self.robot_pos = (robot_row + move_row, robot_col + move_col)
        self.command_pointer += 1
    
    def complete_command(self):
        while self.command_pointer < len(self.command):
            self.execute_move()

    def get_gps_score(self):
        total_score = 0
        for row in range(len(self.map)):
            for col in range(len(self.map[0])):
                if self.map[row][col] == "O":
                    total_score += (100 * row + col)
        return total_score



with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    data = [x.strip() for x in f.readlines()]
    map = [list(x) for x in data if "#" in x]
    command = list("".join([x for x in data if "#" not in x and len(x) > 0]))

warehouse = Warehouse(map, command)
warehouse.complete_command()
print(f"Puzzle 1: {warehouse.get_gps_score()}")