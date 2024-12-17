import os
from typing import List


def checksum(s: List[int]):
    ans = 0
    for i in range(0, len(s)):
        ans += i * (s[i] or 0)
    return ans


def build_map(s: str):
    ans = []
    for i in range(0, len(s)):
        if i % 2 == 0:
            ans.extend([i // 2 for _ in range(int(s[i]))])
        else:
            ans.extend([None for _ in range(int(s[i]))])
    return ans


def move_block_puzzle1(s: List[int]):
    left = 0
    right = len(s) - 1
    while left < right:
        while s[left] is not None:
            left += 1
        while s[right] is None:
            right -= 1
        if left < right:
            s[left], s[right] = s[right], s[left]

    return s


def scan_empty_space(s: List[int], space_needed: int):
    left = s.index(None)
    while left < len(s):
        while s[left] is not None:
            left += 1
        right = left
        while right < len(s) and s[right] is None:
            right += 1
        if right - left >= space_needed:
            return left
        else:
            try:
                left = s.index(None, right)
            except ValueError:
                return None  # No space


def scan_block_size(s: List[int], file_id: int):
    left = s.index(file_id)
    right = left
    while right < len(s) and s[right] == file_id:
        right += 1
    return right - left


def move_block_puzzle2(s: List[int]):
    file_id = max([x for x in s if x is not None])
    while file_id > 0:
        from_left = s.index(file_id)
        block_size = scan_block_size(s, file_id)
        to_left = scan_empty_space(s, block_size)

        if to_left is not None and to_left < from_left:
            # Move file
            for i in range(0, block_size):
                s[from_left + i], s[to_left + i] = s[to_left + i], s[from_left + i]

        file_id -= 1
    return s


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    map = build_map(f.readline().strip())

print(f"Puzzle 1: {checksum(move_block_puzzle1(map.copy()))}")
print(f"Puzzle 2: {checksum(move_block_puzzle2(map.copy()))}")
