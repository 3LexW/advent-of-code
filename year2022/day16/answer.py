import os
import re
from pprint import pp
import itertools
from typing import List


class Graph:
    nodes: {str: int}
    connections: {str: list[str]}
    important_nodes: [str]
    important_paths: {str: int} = {}
    puzzle1_ans: int

    def puzzle1(self, current_node: str, minutes: int, targets: List[str]) -> int:
        # Remove current node
        if current_node in targets:
            targets.remove(current_node)

        if len(targets) == 0 or minutes < 0:
            return 0

        max_score = 0
        for target in targets:
            time = self.important_paths[self.get_key(current_node, target)]
            remaining_time = minutes - time - 1  # Travel time and valve open time
            score = remaining_time * nodes[target]
            max_score = max(
                max_score, self.puzzle1(target, remaining_time, targets.copy()) + score
            )

        return max_score

    def bfs(self, from_node: str, to_node: str) -> int:
        visited = []
        if from_node == to_node:
            return 0
        stack = [[from_node, 0]]
        while stack:
            current_node, step = stack.pop(0)
            if current_node == to_node:
                return step

            if current_node in visited:
                continue

            for conn in self.connections[current_node]:
                stack.append([conn, step + 1])
            visited.append(current_node)

    def get_key(self, from_node: int, to_node: int):
        return f"{from_node} -> {to_node}"

    def __init__(self, nodes: {str: int}, connections: {str: list[str]}) -> None:
        self.nodes = nodes
        self.connections = connections
        self.important_nodes = [k for k, v in self.nodes.items() if v > 0] + ["AA"]
        for start, end in itertools.product(self.important_nodes, self.important_nodes):
            if start == end:
                continue
            self.important_paths[self.get_key(start, end)] = self.bfs(start, end)
        self.puzzle1_ans = self.puzzle1("AA", 30, self.important_nodes)

        print(f"Puzzle 1: {self.puzzle1_ans}")


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

nodes, connections = {}, {}
for line in lines:
    pattern = r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)"
    node_name, flow_rate, valve_connections = re.match(pattern, line).groups()
    nodes[node_name] = int(flow_rate)
    connections[node_name] = valve_connections.split(", ")

g = Graph(nodes, connections)
