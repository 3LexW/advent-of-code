from math import floor, prod
import os
import re
from operator import add, sub, mul, attrgetter
from typing import List, Tuple


class Monkey:
    id: int
    items: List[int]
    operation: str
    test_divisible_by: int
    test_true_to: int
    test_false_to: int
    inspect_cnt: int = 0

    def __init__(
        self,
        id: int,
        items: List[int],
        operation: str,
        test_divisible_by: int,
        test_true_to: int,
        test_false_to: int,
    ) -> None:
        self.id = int(id)
        self.items = list([int(x) for x in items])
        self.operation = operation
        self.test_divisible_by = int(test_divisible_by)
        self.test_true_to = int(test_true_to)
        self.test_false_to = int(test_false_to)

    def throw_item(self) -> List[Tuple[int, int]]:
        """Complete the a round's operation for a monkey, provide a list of list, each list has two entries [next_monkey_id, worry_level]"""
        self._run_operation()
        items = self.items.copy()
        self.items = []  # Remove all items
        res = []
        for item in items:
            to = (
                self.test_true_to
                if item % self.test_divisible_by == 0
                else self.test_false_to
            )
            res.append((to, item))
        return res

    def catch_item(self, to_monkey_id: int, item: int):
        """item should be size of 2, first is the ID, the second one is the item with worry level"""
        if to_monkey_id != self.id:
            raise Exception(
                f"Item should assign to monkey {to_monkey_id}, receiver is {self.id}"
            )
        self.items.append(item)

    def _run_operation(self):
        """Run the operation and return the list new worry levels"""
        operators = {
            "+": add,
            "-": sub,
            "*": mul,
        }
        left, operator, right = re.match(
            r"new = (.*) ([+\-*]) (.*)", self.operation
        ).groups()

        left = self.items  # Always 'old'
        right = int(right) if right.isnumeric() else self.items
        operator = operators.get(operator)

        if not operator:
            raise Exception("Unknown operator")

        if isinstance(right, int):
            self.items = [
                int(floor(operator(left[i], right) / 3)) for i in range(0, len(left))
            ]
        else:
            self.items = [
                int(floor(operator(left[i], right[i]) / 3)) for i in range(0, len(left))
            ]
        self.inspect_cnt += len(self.items)


monkeys: List[Monkey] = []
with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    line = None
    while line != "":
        id = re.match(r".*Monkey (\d+)", f.readline()).groups()[0]
        items = [
            int(x)
            for x in (
                re.match(r".*Starting items: (.*)", f.readline())
                .groups()[0]
                .split(", ")
            )
        ]
        operation = re.match(r".*Operation: (.*)", f.readline()).groups()[0]
        test_divisible_by = re.match(
            r".*Test: divisible by (\d+)", f.readline()
        ).groups()[0]
        test_true_to = re.match(
            r".*If true: throw to monkey (\d+)", f.readline()
        ).groups()[0]
        test_false_to = re.match(
            r".*If false: throw to monkey (\d+)", f.readline()
        ).groups()[0]

        monkeys.append(
            Monkey(
                id=id,
                items=items,
                operation=operation,
                test_divisible_by=test_divisible_by,
                test_true_to=test_true_to,
                test_false_to=test_false_to,
            )
        )

        line = f.readline()

    for _ in range(0, 20):
        for monkey in monkeys:
            items_to_throw = monkey.throw_item()
            for id, item in items_to_throw:
                monkeys[id].catch_item(id, item)

top_two_inspect = sorted(monkeys, key=attrgetter("inspect_cnt"))
print(f"Puzzle 1: {prod([x.inspect_cnt for x in top_two_inspect[-2:]])}")
