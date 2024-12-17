import os
from typing import List


class Computer:
    a: int
    b: int
    c: int
    program: List[int]
    output: List[int]
    pointer: int

    def __init__(self, a, b, c, program):
        self.a = a
        self.b = b
        self.c = c
        self.program = program
        self.output = []
        self.pointer = 0

    def __str__(self):
        return f"Compter: ({self.a}, {self.b}, {self.c}), Program: {self.program}, Pointer: {self.pointer}, Output: {self.output}"

    def full_execute(self):
        while not self.check_program_complete():
            self.execute()

    def check_prefix(self) -> bool:
        return self.output == self.program[:len(self.output)]
    
    def check_program_complete(self) -> bool:
        return not self.pointer < len(self.program)

    def execute(self):
        opcode = self.program[self.pointer]
        literal_operand = self.program[self.pointer + 1]

        jump_pointer = True

        match literal_operand:
            case 4:
                combo_operand = self.a
            case 5:
                combo_operand = self.b
            case 6:
                combo_operand = self.c
            case 7:
                combo_operand = None
            case _:
                combo_operand = literal_operand

        match opcode:
            case 0:  # adv
                self.a = int(self.a / (2**combo_operand))
            case 1:  # blx
                self.b = self.b ^ literal_operand
            case 2:  # bst
                self.b = combo_operand % 8
            case 3:  # jnz
                if self.a != 0:
                    jump_pointer = False
                    self.pointer = literal_operand
            case 4:  # bxc
                self.b = self.b ^ self.c
            case 5:  # out
                self.output.append(combo_operand % 8)
            case 6:  # bdv
                self.b = int(self.a / (2**combo_operand))
            case 7:  # cdv
                self.c = int(self.a / (2**combo_operand))

        if jump_pointer:
            self.pointer += 2


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    data = [x.strip() for x in f.readlines()]

a, b, c = [int(data[i].split(": ")[1]) for i in range(3)]
program = list(map(int, data[4].split(": ")[1].split(",")))

comp = Computer(a, b, c, program)
print(comp)

comp.full_execute()

print(f"Puzzle 1: {",".join([str(x) for x in comp.output])}")