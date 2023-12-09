import os
from typing import List, Tuple


class Board:
    """All use (x, y) for positioning"""

    block_pos: List[str] = []
    current_piece_pos: List[Tuple[int]] = None
    current_piece_id: int = None
    current_piece_cnt: int = None

    moves: str
    current_move_id: int = None

    locked_cnt: int = 0

    def __init__(self, moves: str) -> None:
        self.moves = moves

    def next_frame(self) -> None:
        if not self.current_piece_pos:
            self.current_piece_pos = self.get_next_piece()

        # Horizontal shift, stay original position if reject
        x_shift = self.get_next_move()
        move_attempt = [(x + x_shift, y) for x, y in self.current_piece_pos]
        if not self.check_collision(move_attempt):
            self.current_piece_pos = move_attempt

        # Vertical shift, lock the piece if collisions, else make the shift
        move_attempt = [(x, y - 1) for x, y in self.current_piece_pos]
        if self.check_collision(move_attempt):
            self.block_pos = self.block_pos + self.current_piece_pos
            self.current_piece_pos = None
            self.locked_cnt += 1
        else:
            self.current_piece_pos = move_attempt

    def check_collision(self, target_pos: List[Tuple[int]]) -> bool:
        if len([x for x, _ in target_pos if x < 0 or x >= 7]) > 0 or len(
            [y for _, y in target_pos if y < 0]
        ):
            return True

        for p in target_pos:
            if p in self.block_pos:
                return True

        return False

    def get_next_move(self) -> str:
        if self.current_move_id is None or self.current_move_id == len(self.moves) - 1:
            self.current_move_id = -1
        self.current_move_id += 1
        return -1 if self.moves[self.current_move_id] == "<" else 1

    def get_next_piece(self) -> List[Tuple[int]]:
        if self.current_piece_id is None or self.current_piece_id == 4:
            self.current_piece_id = -1

        self.current_piece_id += 1

        match self.current_piece_id:
            case 0:
                positions = self.get_hor_line_piece()
            case 1:
                positions = self.get_cross_price()
            case 2:
                positions = self.get_reverse_l_piece()
            case 3:
                positions = self.get_ver_line_piece()
            case 4:
                positions = self.get_block_piece()

        # Find the initial position
        highest_block = (
            max([y for _, y in self.block_pos]) if len(self.block_pos) > 0 else -1
        )

        return [(x + 2, y + 4 + highest_block) for x, y in positions]

    def get_hor_line_piece(self) -> List[Tuple[int]]:
        return [(0, 0), (1, 0), (2, 0), (3, 0)]

    def get_cross_price(self) -> List[Tuple[int]]:
        return [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]

    def get_reverse_l_piece(self) -> List[Tuple[int]]:
        return [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

    def get_ver_line_piece(self) -> List[Tuple[int]]:
        return [(0, 0), (0, 1), (0, 2), (0, 3)]

    def get_block_piece(self) -> List[Tuple[int]]:
        return [(0, 0), (0, 1), (1, 0), (1, 1)]

    def draw_board(self) -> List[str]:
        for row in range(max([y for _, y in self.block_pos]), -1, -1):
            x_to_print = [x for x, y in self.block_pos if y == row]
            print(
                f"|{''.join(['#' if i in x_to_print else '.' for i in range(0, 7)])}|"
            )

        print("+-------+")


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    moves = f.readline().strip()

board = Board(moves)
while board.locked_cnt != 2022:
    board.next_frame()
# board.draw_board()

print(f"Puzzle 1: {max([y for x, y in board.block_pos]) + 1}")