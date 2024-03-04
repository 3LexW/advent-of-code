import os
from typing import List, Tuple

class Map:
    elves: List[Tuple[int, int]] = []
    round = 0

    def __init__(self, input: List[str]) -> None:
        for y, line in enumerate(input):
            for x, char in enumerate(line):
                if char == "#":
                    self.elves.append((x, y))

    def can_move(self, x_pos: int, y_pos: int) -> bool:
        # Check if any 8 adjacent location is occupied, if so return True
        shifts = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        for x, y in shifts:
            if (x_pos + x, y_pos + y) in self.elves:
                return True
        return False

    def can_shift_north(self, x_pos: int, y_pos: int) -> bool:
        north_checks = [(0, -1), (1, -1), (-1, -1)]
        for x, y in north_checks:
            if (x_pos + x, y_pos + y) in self.elves:
                return False
        return True

    def can_shift_south(self, x_pos: int, y_pos: int) -> bool:
        south_checks = [(0, 1), (1, 1), (-1, 1)]
        for x, y in south_checks:
            if (x_pos + x, y_pos + y) in self.elves:
                return False
        return True

    def can_shift_east(self, x_pos: int, y_pos: int) -> bool:
        east_checks = [(1, 0), (1, 1), (1, -1)]
        for x, y in east_checks:
            if (x_pos + x, y_pos + y) in self.elves:
                return False
        return True

    def can_shift_west(self, x_pos: int, y_pos: int) -> bool:
        west_checks = [(-1, 0), (-1, 1), (-1, -1)]
        for x, y in west_checks:
            if (x_pos + x, y_pos + y) in self.elves:
                return False
        return True

    def move(self) -> bool:
        next_elves: List[List[Tuple[int, int]]] = []
        call_order = {
            0: (self.can_shift_north, 0, -1),
            1: (self.can_shift_south, 0, 1),
            2: (self.can_shift_west, -1, 0),
            3: (self.can_shift_east, 1, 0),
        }

        for elf in self.elves:
            x, y = elf
            if self.can_move(x, y):
                shirt_success = False
                for round in range(0, 4):
                    func, x_shift, y_shift = call_order[(round + self.round)%4]
                    if func(x, y):
                        next_elves.append([(x, y), (x + x_shift, y + y_shift)])
                        shirt_success = True
                        break
                if not shirt_success:
                    next_elves.append([(x, y), elf])
            else:
                next_elves.append([(x, y), elf])
        # Check the second element of each tuple in next_elves, if it has duplicate, use the first element, else use the second element
        duplicated_moves = [x[1] for x in next_elves]
        duplicated_moves = [x for x in duplicated_moves if duplicated_moves.count(x) > 1]

        next_move = []
        for elf, elf_next_move in next_elves:
            if elf_next_move in duplicated_moves:
                next_move.append(elf)
            else:
                next_move.append(elf_next_move)

        if self.elves == next_move:
            return False
        else:
            self.elves = next_move
            self.round += 1
            return True

    def get_empty_tiles(self) -> int:
        x_min = min([x[0] for x in self.elves])
        x_max = max([x[0] for x in self.elves])
        y_min = min([x[1] for x in self.elves])
        y_max = max([x[1] for x in self.elves])

        return (y_max - y_min + 1) * (x_max - x_min + 1) - len(self.elves)

    def print(self) -> None:
        x_min = min([x[0] for x in self.elves])
        x_max = max([x[0] for x in self.elves])
        y_min = min([x[1] for x in self.elves])
        y_max = max([x[1] for x in self.elves])

        print('====================')
        for y in range(y_min, y_max + 1):
            line = ""
            for x in range(x_min, x_max + 1):
                if (x, y) in self.elves:
                    line += "#"
                else:
                    line += "."
            print(line)
        print('====================')



with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    input = [x.strip() for x in f.read().splitlines()]
    map = Map(input)
    while map.move():
        print(f'Round: {map.round}', end='\r')
        if map.round == 10:
            print(f'Puzzle 1: {map.get_empty_tiles()}')

    print(f'Puzzle 2: {map.round + 1}')
