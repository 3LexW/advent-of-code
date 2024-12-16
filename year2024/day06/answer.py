import os

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    graph = [x.strip() for x in f.readlines()]

tr = len(graph)
tc = len(graph[0])

shifts = [(0, -1), (1, 0), (0, 1), (-1, 0)]
direction = 0  # Using (0, -1) as movement
visited = set()

cr = [r for r in range(0, tr) if "^" in graph[r]][0]
cc = graph[cr].index('^')

def get_next_step(graph, cr, cc, shift):
    if not (0 <= cc + shift[0] < tc and 0 <= cr + shift[1] < tr):
        return None
    else:
        return graph[cr + shift[1]][cc + shift[0]]
    

while True:
    visited.add((cr, cc))
    next_step = get_next_step(graph, cr, cc, shifts[direction])

    if next_step is None:
        # Reach endpoint
        print(f"Puzzle 1: {len(visited)}")
        break
    elif next_step == '#':   
        # Simulate a turn
        direction += 1
        direction %= 4
    else:
        cr, cc = cr + shifts[direction][1], cc + shifts[direction][0]
