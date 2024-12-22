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

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for line in f.readlines():
        secret_number = int(line.strip())
        # print(f"Processing secret number: {secret_number}")
        for i in range(2000):
            secret_number = process(secret_number)
        p1 += secret_number

print(f"Puzzle 1: {p1}")