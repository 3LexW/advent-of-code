import os
from functools import lru_cache


@lru_cache(maxsize=None)
def mix(value, secret_number):
    return value ^ secret_number


@lru_cache(maxsize=None)
def prune(value):
    return value % 16777216


def process(secret_number):
    secret_number = mix(secret_number * 64, secret_number)
    secret_number = prune(secret_number)

    secret_number = mix(secret_number // 32, secret_number)
    secret_number = prune(secret_number)

    secret_number = mix(secret_number * 2048, secret_number)
    secret_number = prune(secret_number)

    return secret_number


p1 = 0
p2 = {}

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for line in f.readlines():
        secret_number = int(line.strip())

        # Set up
        sequence = [secret_number % 10]
        change_seq = []
        seq_value = {}

        # print(f"Processing secret number: {secret_number}")
        for i in range(2000):
            secret_number = process(secret_number)

            sequence.append(secret_number % 10)
            change_seq.append(sequence[-1] - sequence[-2])
            if len(change_seq) == 4:
                if tuple(change_seq) not in seq_value:
                    seq_value[tuple(change_seq)] = sequence[-1]
                sequence.pop(0)
                change_seq.pop(0)

        p1 += secret_number
        for key, price in seq_value.items():
            if key not in p2:
                p2[key] = 0
            p2[key] = p2[key] + price

print(f"Puzzle 1: {p1}")
print(f"Puzzle 2: {max(p2.values())}")
