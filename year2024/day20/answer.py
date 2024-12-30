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
    graph[row][col] = score
    paths.append((row, col))
    for dr, dc in shifts:
        if not 0 <= row + dr < height or not 0 <= col + dc < width:
            continue  # Not a valid point
        if graph[row + dr][col + dc] not in ["S", "E", "."]:
            continue
        heapq.heappush(queue, (score + 1, row + dr, col + dc))


def get_cheat_paths(max_cheat, threshold):
    ans = 0
    for from_r in range(height):
        for from_c in range(width):
            if graph[from_r][from_c] == "#":
                continue
            for radius in range(2, max_cheat + 1):
                for shift_r in range(radius + 1):
                    shift_c = radius - shift_r
                    loop = [
                        (from_r + shift_r, from_c + shift_c),
                        (from_r + shift_r, from_c - shift_c),
                        (from_r - shift_r, from_c + shift_c),
                        (from_r - shift_r, from_c - shift_c),
                    ]
                    if shift_r == 0:
                        loop.remove((from_r - shift_r, from_c + shift_c))
                        loop.remove((from_r - shift_r, from_c - shift_c))
                    if shift_c == 0:
                        loop.remove((from_r + shift_r, from_c - shift_c))
                        loop.remove((from_r - shift_r, from_c - shift_c))

                    for to_r, to_c in loop:
                        if not (0 <= to_r < height and 0 <= to_c < width):
                            continue  # Out of bound
                        if graph[to_r][to_c] == "#":
                            continue  # Cheat failed
                        time_saved = graph[to_r][to_c] - graph[from_r][from_c]
                        if time_saved >= threshold + radius:
                            ans += 1
    return ans


p1 = get_cheat_paths(2, 100)
print(f"Puzzle 1: {p1}")

p2 = get_cheat_paths(20, 100)
print(f"Puzzle 2: {p2}")
