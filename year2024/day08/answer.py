import os
from typing import Dict, Tuple, List
from pprint import pp

p1 = set()
p2 = set()
antennas: Dict[str, List[Tuple[int, int]]] = {}


def validate_loaction(graph, node):
    total_row = len(graph)
    total_col = len(graph[0])
    return 0 <= node[0] < total_row and 0 <= node[1] < total_col


def get_antinode(from_node, to_node, multiplier=1):
    diff = (
        (from_node[0] - to_node[0]) * multiplier,
        (from_node[1] - to_node[1]) * multiplier,
    )
    return (to_node[0] - diff[0], to_node[1] - diff[1])


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    graph = [x.strip() for x in f.readlines()]
    total_row = len(graph)
    total_col = len(graph[0])

# Obtain the important nodes
for row in range(0, total_row):
    for col in range(0, total_col):
        char = graph[row][col]
        if char == ".":
            continue
        if char not in antennas.keys():
            antennas[char] = []
        antennas[char].append((row, col))

# Check each node type
for key, nodes in antennas.items():
    for i in range(0, len(nodes)):
        for j in range(i + 1, len(nodes)):
            multiplier = 1
            while True:
                node1 = get_antinode(nodes[i], nodes[j], multiplier)
                if validate_loaction(graph, node1):
                    if multiplier == 1:
                        p1.add(node1)
                    p2.add(node1)
                    multiplier += 1
                else:
                    break

            multiplier = 1
            while True:
                node2 = get_antinode(nodes[j], nodes[i], multiplier)
                if validate_loaction(graph, node2):
                    if multiplier == 1:
                        p1.add(node2)
                    p2.add(node2)
                    multiplier += 1
                else:
                    break

    # Attenas are also anitnodes
    for node in nodes:
        p2.add(node)


print(f"Puzzle 1: {len(p1)}")
print(f"Puzzle 2: {len(p2)}")
