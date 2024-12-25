import os

keys = []
locks = []

def map_to_array(map, check_key):
    array = [0, 0, 0, 0 ,0]
    for row in range(1, len(map) - 1):
        for col in range(len(map[0])):
            if map[row][col] == check_key:
                array[col] += 1
    return array


def read_map(map):
    if map[0][0] == '#':
        locks.append(map_to_array(map, '#'))
        return
    if map[0][0] == '.':
        keys.append(map_to_array(map, '#'))
        return

def match(key, lock):
    return max([key[i] + lock[i]for i in range(5)]) <= 5


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    map = []
    line = f.readline()

    while len(line) > 0:
        if len(line.strip()) == 0:
            read_map(map)
            map = []
        else:
            map.append(line.strip())
        line = f.readline()
    read_map(map)

ans = 0
for lock in locks:
    for key in keys:
        if match(key, lock): 
            # print(lock, key)
            ans += 1

print(f"Puzzle: {ans}")