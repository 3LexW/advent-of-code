import os, re

check_y = 2000000
checked = set()
beacons = []

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
        if y_shift > max_distance:
            continue

        print(f"Sensor has covered row {check_y}: {sensor} to {beacon}")

        x_shift = abs(max_distance - y_shift)
        print(
            f"X can shift from {(sensor_x - x_shift, check_y)} to {(sensor_x + x_shift, check_y)}"
        )
        for x in range(sensor_x - x_shift, sensor_x + x_shift + 1):
            checked.add((x, check_y))

no_beacon_checked = [x for x in checked if x not in beacons]
print(f"Puzzle 1: {len(no_beacon_checked)}")