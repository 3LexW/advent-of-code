import os
from typing import Dict, List, Set
from pprint import pp

graph: Dict[int, Set[int]] = (
    {}
)  # Key: page number # Value: list of page number before it
p1 = 0
p2 = 0


def validate_update(graph, update):
    for i in range(len(update) - 1, 0, -1):
        if update[i] not in graph or update[i - 1] not in graph[update[i]]:
            return i
    return None


def fix_update(graph, update: List[int]):
    wrong_index = validate_update(graph, update)
    while wrong_index is not None:
        number_to_shift = update.pop(wrong_index)
        update.insert(0, number_to_shift)
        wrong_index = validate_update(graph, update)

    return update


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    rule = f.readline().strip()
    while len(rule.strip()) > 0:
        before, after = map(int, rule.split("|"))
        if after not in graph.keys():
            graph[after] = set()
        graph[after].add(before)
        rule = f.readline().strip()

    # Now, update the graph so that all the intermediate nodes are inserted
    updates = [list(map(int, x.strip().split(","))) for x in f.readlines()]
    for update in updates:
        if validate_update(graph, update) is None:
            p1 += update[(len(update) // 2)]
        else:
            p2 += fix_update(graph, update)[(len(update) // 2)]

print(f"Puzzle 1: {p1}")
print(f"Puzzle 1: {p2}")
