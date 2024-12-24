import os
from functools import cache
from itertools import product
from pprint import pp
from math import inf


def _bfs(layout, from_key, to_key):
    movements = [
        ("^", -1, 0),
        (">", 0, 1),
        ("v", 1, 0),
        ("<", 0, -1),
    ]
    height = len(layout)
    width = len(layout[0])
    visited = {}
    stack = [(from_key, "")]

    while len(stack) > 0:
        current_key, moves = stack.pop(0)

        if current_key not in visited or len(moves + "A") < len(
            visited[current_key][0]
        ):
            visited[current_key] = [moves + "A"]
        elif len(moves + "A") == len(visited[current_key][0]):
            visited[current_key].append(moves + "A")
        else:
            continue

        current_row = [i for i, row in enumerate(layout) if current_key in row][0]
        current_col = layout[current_row].index(current_key)

        for step, row_shift, col_shift in movements:
            new_row, new_col = current_row + row_shift, current_col + col_shift
            if not (0 <= new_row < height and 0 <= new_col < width):
                continue
            if layout[new_row][new_col] is None:
                continue
            stack.append((layout[new_row][new_col], moves + step))

    return visited[to_key]


def _set_move_map(move_map, layout):
    keys = [x for x in sum(layout, []) if x is not None]
    for i in range(0, len(keys)):
        for j in range(0, len(keys)):
            if (keys[i], keys[j]) not in move_map:
                move_map[(keys[i], keys[j])] = set()
            move_map[(keys[i], keys[j])].update(_bfs(layout, keys[i], keys[j]))
    return move_map


move_map = {}
numpad_layout = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"],
]
move_map = _set_move_map(move_map, numpad_layout)

keypad_layout = [[None, "^", "A"], ["<", "v", ">"]]
move_map = _set_move_map(move_map, keypad_layout)


@cache
def get_length(from_key, to_key, depth=2):
    if depth == 1:
        return len(list(move_map.get((from_key, to_key)))[0])
    min_length = inf
    for step in move_map[(from_key, to_key)]:
        length = 0
        for a, b in zip("A" + step, step):
            length += get_length(a, b, depth - 1)
        min_length = min(min_length, length)
    return min_length


def solve(s):
    current_step = "A"
    ans = set([""])
    for next_step in list(s):
        current_ans = move_map[(current_step, next_step)]
        ans = set([a + b for (a, b) in product(ans, current_ans)])
        min_len = len(min(ans, key=lambda x: len(x)))
        ans = [x for x in ans if len(x) == min_len]

        current_step = next_step
    return ans


p1 = 0
p2 = 0

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for goal in [x.strip() for x in f.readlines()]:
        num_val = int(goal.replace("A", ""))
        possible_paths = solve(goal)

        # Solve p1
        min_length = inf
        for p in possible_paths:
            current_pos = "A"
            current_length = 0
            for next_key in p:
                current_length += get_length(current_pos, next_key, 2)
                current_pos = next_key
            min_length = min(min_length, current_length)

        p1 += num_val * min_length

        # Solve p2
        min_length = inf
        for p in possible_paths:
            current_pos = "A"
            current_length = 0
            for next_key in p:
                current_length += get_length(current_pos, next_key, 25)
                current_pos = next_key
            min_length = min(min_length, current_length)

        p2 += num_val * min_length


print(f"Puzzle 1: {p1}")
print(f"Puzzle 2: {p2}")
