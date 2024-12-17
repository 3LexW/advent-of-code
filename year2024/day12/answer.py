import os
from pprint import pp

global total_r
global total_c
global p1_map
global visited_nodes

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    graph = [x.strip() for x in f.readlines()]

total_r = len(graph)
total_c = len(graph[0])
visited_nodes = set()

shifts = [(1, 0), (-1, 0), (0, 1), (0, -1)]

p1 = 0


def get_neighbor_nodes(graph, r, c):
    ans = set()
    ans.add((r, c))
    current_node = graph[r][c]
    visited_nodes.add((r, c))
    for shift_r, shift_c in shifts:
        if (r + shift_r, c + shift_c) in visited_nodes:
            continue
        if not (0 <= r + shift_r < total_r) or not (0 <= c + shift_c < total_c):
            continue
        if graph[r + shift_r][c + shift_c] != current_node:
            continue
        ans.add((r + shift_r, c + shift_c))

        extra_nodes = get_neighbor_nodes(graph, r + shift_r, c + shift_c)
        if extra_nodes is not None:
            ans.update(extra_nodes)

    return ans


def calculate_sides(graph, nodes):
    count = len(nodes)
    sides = 0
    for [r, c] in nodes:
        current_node = graph[r][c]
        for shift_r, shift_c in shifts:
            if not (0 <= r + shift_r < total_r) or not (0 <= c + shift_c < total_c):
                sides += 1  # Out of bound = need fence
                continue
            if graph[r + shift_r][c + shift_c] != current_node:
                sides += 1  # Reach other nodes = need fence
                continue

    print(current_node, count, sides, count * sides)
    return count * sides


for r in range(total_r):
    for c in range(total_c):
        if (r, c) in visited_nodes:
            continue  # Calculated
        nodes_to_calculate = get_neighbor_nodes(graph, r, c)
        p1 += calculate_sides(graph, nodes_to_calculate)

print(f"Puzzle 1: {p1}")
