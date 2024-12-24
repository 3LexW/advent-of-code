import os
import heapq

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    graph = [list(x.strip()) for x in f.readlines()]

height = len(graph)
width = len(graph[0])

start_row = [i for i, x in enumerate(graph) if "S" in x][0]
start_col = graph[start_row].index("S")
end_row = [i for i, x in enumerate(graph) if "E" in x][0]
end_col = graph[end_row].index("E")

shifts = [(-1, 0), (0, 1), (1, 0), (0, -1)]

queue = [(0, start_row, start_col)]
paths = []
while queue:
    score, row, col = heapq.heappop(queue)
    paths.append((row, col))
    for dr, dc in shifts:
        if not 0 <= row + dr < height or not 0 <= col + dc < width:
            continue  # Not a valid point
        if graph[row + dr][col + dc] == "#":
            continue
        if (row + dr, col + dc) in paths:
            continue
        heapq.heappush(queue, (score + 1, row + dr, col + dc))


def get_cheat_paths(max_cheat):
    ans = {}
    for i in range(len(paths)):
        (from_r, from_c) = paths[i]
        for j in range(i + 1, len(paths)):
            if j - i <= max_cheat:
                continue  # You can just walk to it
            (to_r, to_c) = paths[j]
            distance = abs(to_r - from_r) + abs(to_c - from_c)
            if distance <= max_cheat:
                if j - i - max_cheat not in ans:
                    ans[j - i - max_cheat] = 0
                ans[j - i - max_cheat] = ans[j - i - max_cheat] + 1
    return dict(sorted(ans.items()))


p1 = get_cheat_paths(2)
print(p1)
print(f"Puzzle 1: {sum([value for key, value in p1.items() if key >= 100])}")
