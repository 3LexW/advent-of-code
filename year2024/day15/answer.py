import os
from pprint import pp
from typing import List, Tuple
from copy import deepcopy


class Warehouse:
    map: List[List[str]]
    command: List[str]
    command_pointer: int
    robot_pos: Tuple[int, int]

    def __init__(self, map, command, expand=False):
        self.map = map
        self.command = command
        if expand:
            self.map = self.get_expand_map()
        robot_row = [i for i, x in enumerate(self.map) if "@" in x][0]
        robot_col = [j for j, row in enumerate(self.map[robot_row]) if "@" in row][0]
        self.robot_pos = (robot_row, robot_col)
        self.command_pointer = 0

    def _get_extended_tile(_, tile):
        match tile:
            case "#":
                return ["#", "#"]
            case "O":
                return ["[", "]"]
            case ".":
                return [".", "."]
            case "@":
                return ["@", "."]

    def get_expand_map(self):
        expanded_map = []
        for row in self.map:
            new_row = []
            for col in row:
                new_row.extend(self._get_extended_tile(col))
            expanded_map.append(new_row)
        return expanded_map

    def _get_current_command(self):
        return self.command[self.command_pointer]

    def _get_move(self):
        match self._get_current_command():
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

        current_move = self._get_current_command()
        move_row, move_col = self._get_move()
        self.command_pointer += 1

        stack = [(robot_row + move_row, robot_col + move_col, "@")]
        move_to_do = {(robot_row, robot_col): "."}

        while len(stack) > 0:
            row, col, next_val = stack.pop()

            if (row, col) in move_to_do.keys() and move_to_do[(row, col)] != ".":
                continue  # Visited

            if self.map[row][col] == "#":
                return  # Do nothing

            if self.map[row][col] == ".":
                move_to_do[(row, col)] = next_val
                continue  # Valid

            if self.map[row][col] == "O" or self.map[row][col] in "[]":  # Puzzle 1
                move_to_do[(row, col)] = next_val
                stack.append((row + move_row, col + move_col, self.map[row][col]))

            if self.map[row][col] in "[]" and current_move in "^v":
                match self.map[row][col]:
                    case "[":  # Check right
                        stack.append((row, col + 1, "."))
                    case "]":
                        stack.append((row, col - 1, "."))
                    case _:
                        self.print_map()
                        raise ValueError(
                            "It is not a legit warehouse map since box pattern is not good"
                        )

        # Move the points if valid
        for (row, col), next_val in move_to_do.items():
            self.map[row][col] = next_val
        self.robot_pos = (robot_row + move_row, robot_col + move_col)

    def complete_command(self):
        while self.command_pointer < len(self.command):
            self.execute_move()
            # self.print_map()

    def get_gps_score(self):
        total_score = 0
        for row in range(len(self.map)):
            for col in range(len(self.map[0])):
                if self.map[row][col] in "O[":
                    total_score += 100 * row + col
        return total_score

    def print_map(self):
        print("\n".join(["".join(row) for row in self.map]))


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    data = [x.strip() for x in f.readlines()]
    map = [list(x) for x in data if "#" in x]
    command = list("".join([x for x in data if "#" not in x and len(x) > 0]))

warehouse = Warehouse(deepcopy(map), command, False)
warehouse.complete_command()
warehouse.print_map()
print(f"Puzzle 1: {warehouse.get_gps_score()}\n")

warehouse = Warehouse(deepcopy(map), command, True)
warehouse.complete_command()
warehouse.print_map()
print(f"Puzzle 2: {warehouse.get_gps_score()}\n")
