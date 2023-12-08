import os
import re
import itertools


def split_range(
    range_from: int, range_to: int, cut_from: int, cut_to: int
) -> [int, int]:
    """Split a range into three parts, the left, the cut, and the right"""
    left = None if range_from >= cut_from else [range_from, min(cut_from - 1, range_to)]
    right = None if range_to <= cut_to else [max(cut_to + 1, range_from), range_to]
    cut = (
        None
        if range_to < cut_from or range_from > cut_to
        else [max(cut_from, range_from), min(cut_to, range_to)]
    )

    return left, cut, right


def get_mapping(source_from: int, dest_from: int, length: int, value: int) -> int:
    if source_from <= value <= source_from + length - 1:
        return dest_from + (value - source_from)
    else:
        return value


def get_next_round(
    source_from: [int], dest_from: [int], length: [int], value: [int, int]
) -> [[int, int]]:
    if len(source_from) != len(dest_from):
        raise Exception("source_from and dest_from should share the same size")

    to_be_mapped = [value]  # The stack of list to be mapped
    mapped = []  # The mapped result

    for i in range(0, len(source_from)):
        # Obtain the cut to be transformed
        cut_from, cut_to = [source_from[i], source_from[i] + length[i] - 1]
        to_be_mapped_next_round = []
        while to_be_mapped:
            range_from, range_to = to_be_mapped.pop()
            left, cut, right = split_range(range_from, range_to, cut_from, cut_to)
            if left:
                to_be_mapped_next_round.append(left)
            if right:
                to_be_mapped_next_round.append(right)
            if cut:
                mapped.append(
                    [
                        get_mapping(source_from[i], dest_from[i], length[i], cut[0]),
                        get_mapping(source_from[i], dest_from[i], length[i], cut[1]),
                    ]
                )
        to_be_mapped = to_be_mapped_next_round

    return mapped + to_be_mapped_next_round


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    inputs = [
        int(x)
        for x in re.match(r"seeds: ([\d ]+)", f.readline()).groups()[0].split(" ")
    ]

    p1_ranges = [[x, x] for x in inputs]
    p2_ranges = [
        [inputs[i], inputs[i] + inputs[i + 1] - 1] for i in range(0, len(inputs), 2)
    ]
    current_step_p1, current_step_p2 = p1_ranges, p2_ranges

    for step_no in range(0, 7):
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
                int(x) for x in re.findall(r"(\d+)", line.strip())
            )
            source_froms.append(source_from)
            dest_froms.append(dest_from)
            lengths.append(length)

        previous_step_p1, previous_step_p2 = current_step_p1, current_step_p2
        current_step_p1, current_step_p2 = [
            list(
                itertools.chain.from_iterable(
                    [
                        get_next_round(source_froms, dest_froms, lengths, x)
                        for x in previous_step
                    ]
                )
            )
            for previous_step in (previous_step_p1, previous_step_p2)
        ]


print(f"Puzzle 1: {min([x[0] for x in current_step_p1])}")
print(f"Puzzle 2: {min([x[0] for x in current_step_p2])}")
