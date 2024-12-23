import os
from copy import deepcopy
from typing import Set
from pprint import pp

map = {}
p1 = set()

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for line in f.readlines():
        node_2 = line.strip().split("-")
        node_1, node_2 = node_2[0], node_2[1]

        if node_1 not in map.keys():
            map[node_1] = []
        if node_2 not in map.keys():
            map[node_2] = []

        map[node_1].append(node_2)
        map[node_2].append(node_1)

# Find 3 inter-connect nodes for t prefix
for node_1 in [key for key in map.keys() if key.startswith("t")]:
    for node_2 in map[node_1]:
        for node_3 in map[node_2]:
            if node_3 in map[node_1]:
                nodes = [node_1, node_2, node_3]
                nodes.sort()

                p1.add(",".join(nodes))

print(f"Puzzle 1: {len(p1)}")

max_cliques = []


def bron_kerbosch(current_clique: Set[str], candidates: Set[str], excluded: Set[str]):
    if len(candidates) == 0 and len(excluded) == 0:
        max_cliques.append(current_clique)
    else:
        to_be_checked = deepcopy(candidates)
        for candidate in to_be_checked:
            new_current = deepcopy(current_clique)
            new_current.add(candidate)

            new_candidates = candidates.intersection(map[candidate])
            new_excluded = excluded.intersection(map[candidate])

            bron_kerbosch(new_current, new_candidates, new_excluded)

            candidates.remove(candidate)
            excluded.add(candidate)


bron_kerbosch(set(), set(map.keys()), set())
largest_clique = list(max(max_cliques, key=lambda clique: len(clique)))
largest_clique.sort()

print(f"Puzzle 2: {",".join(largest_clique)}")
