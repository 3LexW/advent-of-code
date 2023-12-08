import os, re

check_y = 2000000
checked = set()
beacons = []
check_ranges = {}

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for line in f:
        sensor, beacon = map(
            lambda x: (int(x[0]), int(x[1])), re.findall(r"x=(-?\d+), y=(-?\d+)", line)
        )
        beacons.append(beacon)
        sensor_x, sensor_y = sensor
        beacon_x, beacon_y = beacon

        max_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

        y_shift = abs(check_y - sensor_y)
        if y_shift <= max_distance:
            print(f"Sensor {sensor} to beacon {beacon} has covered row {check_y}")

            x_shift = abs(max_distance - y_shift)
            print(
                f"X can shift from  {(sensor_x - x_shift, check_y)} to {(sensor_x + x_shift, check_y)}"
            )
            for x in range(sensor_x - x_shift, sensor_x + x_shift + 1):
                checked.add((x, check_y))

        # Add check ranges
        for y in range(sensor_y - max_distance, sensor_y + max_distance + 1):
            y_shift = abs(y - sensor_y)
            x_shift = abs(max_distance - y_shift)
            if y not in check_ranges:
                check_ranges[y] = []
            check_ranges[y].append([sensor_x - x_shift, sensor_x + x_shift])

no_beacon_checked = [x for x in checked if x not in beacons]
print(f"Puzzle 1: {len(no_beacon_checked)}")

# Puzzle 2
max_check = 4000000

for y in range(0, max_check):
    print(f"Checking line {y}", end="\r")

    check_ranges[y].sort(key = lambda x: x[0])

    wrong_number = None
    full_range = check_ranges[y][0]

    for i in range(1, len(check_ranges[y])):
        full_range_from, full_range_to = full_range
        next_range_from, next_range_to = check_ranges[y][i]
        if full_range_from <= next_range_from <= next_range_to <= full_range_to:
            continue # Full cover
        if next_range_from - full_range_to > 1:
            wrong_number = full_range_to + 1
        full_range = [min(full_range_from, next_range_from), max(full_range_to, next_range_to)]

    if wrong_number:
        print(f"Unchecked range for row {y} found: {check_ranges[y]}")
        print(f"Wrong Number: {wrong_number}")
        print(f"Puzzle 2: {y + 4000000 * wrong_number}")
