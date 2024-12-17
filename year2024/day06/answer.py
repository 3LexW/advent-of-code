import os
import copy
from collections import Counter

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    graph = [list(x.strip()) for x in f.readlines()]

tr = len(graph)
tc = len(graph[0])

shifts = [(0, -1), (1, 0), (0, 1), (-1, 0)]
direction = 0  # Using (0, -1) as movement
visited = set()

start_r = [r for r in range(0, tr) if "^" in graph[r]][0]
start_c = graph[start_r].index("^")


def get_next_step(graph, cr, cc, shift):
    if not (0 <= cc + shift[0] < tc and 0 <= cr + shift[1] < tr):
        return None
    else:
        return graph[cr + shift[1]][cc + shift[0]]


cr, cc = start_r, start_c
while True:
    visited.add((cr, cc))
    next_step = get_next_step(graph, cr, cc, shifts[direction])

    if next_step is None:
        # Reach endpoint
        print(f"Puzzle 1: {len(visited)}")
        break
    elif next_step == "#":
        # Simulate a turn
        direction += 1
        direction %= 4
    else:
        cr, cc = cr + shifts[direction][1], cc + shifts[direction][0]

p2 = 0
for r, c in copy.deepcopy(visited):
    graph_copy = copy.deepcopy(graph)
    graph_copy[r][c] = "#"

    visited = set()
    direction = 0  # Using (0, -1) as movement
    turning_points = []
    cr, cc = start_r, start_c

    while True:
        visited.add((cr, cc))
        next_step = get_next_step(graph_copy, cr, cc, shifts[direction])

        if next_step is None:
            break
        elif next_step == "#":
            # Simulate a turn
            direction += 1
            direction %= 4
            turning_points.append((cr, cc))
            if Counter(turning_points).most_common(1)[0][1] > 3:
                p2 += 1
                break
        else:
            cr, cc = cr + shifts[direction][1], cc + shifts[direction][0]

print(f"Puzzle 2: {p2}")
