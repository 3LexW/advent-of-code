import os
import re
from operator import mul
from functools import reduce
from copy import deepcopy

global width
global height

width = 11
height = 7

width = 101
height = 103

p1 = [0, 0, 0, 0]
all_robots_loc = []


def next_move(px, py, vx, vy):
    return (px + vx) % width, (py + vy) % height, vx, vy


def visualize(robots_loc):
    graph = []
    all_unique = True
    for row in range(height):
        row_graph = []
        for col in range(width):
            cnt = len([x for x in robots_loc if x[0] == col and x[1] == row])
            if cnt == 0:
                row_graph.append(".")
            else:
                row_graph.append(str(cnt))
            if cnt > 1:
                all_unique = False
        graph.append("".join(row_graph))
    if all_unique:
        print("\n")
        print("\n".join(graph))


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    data = "\n".join([x.strip() for x in f.readlines()])
    robots = re.findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", data)

for robot in robots:
    px, py, vx, vy = map(int, robot)
    all_robots_loc.append((px, py, vx, vy))

    for _ in range(100):
        px, py, _, _ = next_move(px, py, vx, vy)

    # Determine quadrants
    if px == width // 2 or py == height // 2:
        continue  # Not in the four quadrants

    if px < width // 2 and py < height // 2:
        p1[0] += 1
    if px > width // 2 and py < height // 2:
        p1[1] += 1
    if px < width // 2 and py > height // 2:
        p1[2] += 1
    if px > width // 2 and py > height // 2:
        p1[3] += 1

print(f"Puzzle 1: {reduce(mul, p1, 1)}")

for i in range(10000):
    new_robots = []
    for robot in all_robots_loc:
        new_robots.append(next_move(robot[0], robot[1], robot[2], robot[3]))
    print(f"Iteration: {i}", end="\r")
    visualize(new_robots)
    all_robots_loc = new_robots
    # input(f"Current iteration: {i}, press enter to continue")
