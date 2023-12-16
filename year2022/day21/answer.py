from functools import cache
import os, re
from typing import Dict, Tuple

numbers: Dict[str, int] = {}
operations: Dict[str, Tuple[str]] = {}


@cache
def get_number(variable: str):
    global numbers, operations
    if variable in numbers:
        return numbers[variable]
    elif variable in operations:
        left, operator, right = operations[variable]
        left = get_number(left)
        right = get_number(right)
        match operator:
            case "+":
                return left + right
            case "-":
                return left - right
            case "*":
                return left * right
            case "/":
                return left / right
            case _:
                raise Exception(f"Unknown operator: {operator}")
    else:
        raise Exception(f"Unknown variable: {variable}")


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

# Register the numbers and operations
number_pattern = r"(\w+): (\d+)"
operation_pattern = r"(\w+): (\w+) ([+\-*/]) (\w+)"

for line in lines:
    number_match = re.match(number_pattern, line)
    operation_match = re.match(operation_pattern, line)

    if number_match:
        variable, number = number_match.groups()
        numbers[variable] = int(number)
    elif operation_match:
        variable, left, op, right = operation_match.groups()
        operations[variable] = (left, op, right)
    else:
        raise Exception(f"Match pattern failed for line: {line}")

print(f"Puzzle 1: {get_number('root')}")


@cache
def has_human(variable: str) -> bool:
    global numbers, operations
    if variable == "humn":
        return True
    elif variable in numbers:
        return False  # Not human
    elif variable in operations:
        left, _, right = operations[variable]
        return has_human(left) or has_human(right)


@cache
def get_human(variable: str, target: int):
    global numbers, operations
    if variable == "humn":
        return target
    elif variable in operations:
        left, operator, right = operations[variable]
        if has_human(left):
            match operator:
                case "+":
                    return get_human(left, target - get_number(right))
                case "-":
                    return get_human(left, target + get_number(right))
                case "*":
                    return get_human(left, target / get_number(right))
                case "/":
                    return get_human(left, target * get_number(right))
                case _:
                    raise Exception(f"Unknown operator: {operator}")
        elif has_human(right):
            match operator:
                case "+":
                    return get_human(right, target - get_number(left))
                case "-":
                    return get_human(right, get_number(left) - target)
                case "*":
                    return get_human(right, target / get_number(left))
                case "/":
                    return get_human(right, get_number(left) / target)
                case _:
                    raise Exception(f"Unknown operator: {operator}")
        else:
            raise Exception("It is impossible to have human on both sides of a node")


left, _, right = operations["root"]
if has_human(left):
    ans = get_human(left, get_number(right))
else:
    ans = get_human(right, get_number(left))

print(f"Puzzle 2: {ans}")
