import os
import re


def get_mapping(source_from: [int], dest_from: [int], length: [int], value) -> int:
    if len(source_from) != len(dest_from):
        raise Exception("source_from and dest_from should share the same size")

    for i in range(0, len(source_from)):
        if source_from[i] <= value <= source_from[i] + length[i] - 1:
            return dest_from[i] + (value - source_from[i])
    return value


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    seeds = [
        int(x)
        for x in re.match(r"seeds: ([\d ]+)", f.readline()).groups()[0].split(" ")
    ]

    current_step = seeds
    for _ in range(0, 7):
        while "map" not in f.readline():
            continue

        dest_froms = []
        source_froms = []
        lengths = []
        while True:
            line = f.readline()
            if len(line.strip()) == 0:
                break
            dest_from, source_from, length = (
                int(x) for x in re.findall(r"(\d+)", line)
            )
            source_froms.append(source_from)
            dest_froms.append(dest_from)
            lengths.append(length)

        previous_step = current_step
        current_step = [
            get_mapping(source_froms, dest_froms, lengths, x) for x in previous_step
        ]


print(f"Puzzle 1: {min(current_step)}")
