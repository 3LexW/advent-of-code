import os
from pprint import pp


def flood(graph, current_point, previous_steps):
    total_r = len(graph)
    total_c = len(graph[0])
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    reached_points = set()
    distinct_paths = 0

    def is_valid(point):
        return 0 <= point[0] < total_r and 0 <= point[1] < total_c

    current_height = graph[current_point[0]][current_point[1]]

    for direction in directions:
        new_point = (current_point[0] + direction[0], current_point[1] + direction[1])
        if new_point in previous_steps:  # Loop
            continue
        if not is_valid(new_point):  # Out of bound
            continue
        if graph[new_point[0]][new_point[1]] != current_height + 1:  # Inreachable
            continue
        if graph[new_point[0]][new_point[1]] == 9:
            reached_points.add(new_point)
            distinct_paths += 1

        new_steps = previous_steps.copy()
        new_steps.append(new_point)

        new_reached_points, new_distinct_paths = flood(graph, new_point, new_steps)

        reached_points.update(new_reached_points)
        distinct_paths += new_distinct_paths

    return reached_points, distinct_paths





with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    graph = [list(map(int, x.strip())) for x in f.readlines()]

total_r = len(graph)
total_c = len(graph[0])
starting_points = []
p1 = 0
p2 = 0

for r in range(total_r):
    for c in range(total_c):
        if graph[r][c] == 0:
            starting_points.append((r, c))

for point in starting_points:
    reached_points, distinct_paths = flood(graph, point, [point])
    p1 += len(reached_points)
    p2 += distinct_paths


print(f"Puzzle 1: {p1}")
print(f"Puzzle 2: {p2}")
