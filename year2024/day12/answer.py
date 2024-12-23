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
p2 = 0


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


def calculate_fence(graph, nodes):
    count = len(nodes)
    fence = 0
    for [r, c] in nodes:
        current_node = graph[r][c]
        for shift_r, shift_c in shifts:
            if not (0 <= r + shift_r < total_r) or not (0 <= c + shift_c < total_c):
                fence += 1  # Out of bound = need fence
                continue
            if graph[r + shift_r][c + shift_c] != current_node:
                fence += 1  # Reach other nodes = need fence
                continue

    # print(current_node, count, fence, count * fence)
    return count * fence


def get_consecutives_in_list(l):
    ans = 0
    if len(l) == 0:
        return ans
    l.sort()
    for i in range(1, len(l)):
        if l[i] - l[i - 1] > 1:
            ans += 1
    return ans + 1


def calculate_sides(graph, nodes):
    count = len(nodes)
    sides = 0

    node_letter = graph[nodes[0][0]][nodes[0][1]]
    left = min(nodes, key=lambda node: node[1])[1]
    right = max(nodes, key=lambda node: node[1])[1]
    top = min(nodes, key=lambda node: node[0])[0]
    bottom = max(nodes, key=lambda node: node[0])[0]

    for r in range(top, bottom + 1):
        top_side = []
        bottom_side = []

        for c in range(left, right + 1):
            if (r, c) not in nodes:
                continue
            if not (0 <= r - 1 < total_r) or graph[r - 1][c] != node_letter:
                top_side.append(c)
            if not (0 <= r + 1 < total_r) or graph[r + 1][c] != node_letter:
                bottom_side.append(c)

        sides += get_consecutives_in_list(top_side)
        sides += get_consecutives_in_list(bottom_side)

    for c in range(left, right + 1):
        left_side = []
        right_side = []

        for r in range(top, bottom + 1):
            if (r, c) not in nodes:
                continue
            if not (0 <= c - 1 < total_c) or graph[r][c - 1] != node_letter:
                left_side.append(r)
            if not (0 <= c + 1 < total_c) or graph[r][c + 1] != node_letter:
                right_side.append(r)

        sides += get_consecutives_in_list(left_side)
        sides += get_consecutives_in_list(right_side)

    # print(node_letter, count, sides, count * sides)
    return count * sides


for r in range(total_r):
    for c in range(total_c):
        if (r, c) in visited_nodes:
            continue  # Calculated
        nodes_to_calculate = get_neighbor_nodes(graph, r, c)
        p1 += calculate_fence(graph, nodes_to_calculate)
        p2 += calculate_sides(graph, list(nodes_to_calculate))

print(f"Puzzle 1: {p1}")
print(f"Puzzle 2: {p2}")
