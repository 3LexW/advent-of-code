import os
from pprint import pprint
import re
from typing import Dict


def cd(pwd: str, next_dir: str) -> str:
    match next_dir:
        case "/":
            return "/"
        case "..":
            if len(pwd.split("/")[:-1]) == 1:
                return "/"
            else:
                return "/".join(pwd.split("/")[:-1])
        case _:
            return f"{pwd}{next_dir}" if pwd == "/" else f"{pwd}/{next_dir}"


def append_file(pwd: str, name: str, size: int, state: Dict[str, int]):
    if pwd == "/":
        state[f"{pwd}{name}"] = size
    else:
        state[f"{pwd}/{name}"] = size
    return state


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

line_no = 0
pwd: str = "/"
files: Dict[str, int] = {}
folders = set()

command_rgx = r"\$ (\w+)( )?(.*)?"
file_line_rgx = r"(\d+) (.*)"


while line_no < len(lines):
    match = re.match(command_rgx, lines[line_no])
    if match:
        command = match.group(1)
        match command:
            case "cd":
                next_dir = match.group(3)
                pwd = cd(pwd, next_dir)
                folders.add(pwd)
                line_no += 1
            case "ls":
                line_no += 1
                while (
                    line_no < len(lines)
                    and re.match(command_rgx, lines[line_no]) == None
                ):
                    if "dir" in lines[line_no]:
                        next = lines[line_no].replace("dir", "").strip()
                        folders.add(cd(pwd, next))
                    else:
                        size, filename = re.match(
                            file_line_rgx, lines[line_no]
                        ).groups()
                        state = append_file(pwd, filename, int(size), files)
                    line_no += 1

    else:
        line_no += 1

folder_sizes = {folder: sum([v for k, v in files.items() if k.startswith(f'{folder}')]) for folder in folders}

print(f'Puzzle 1: {sum([v for k, v in folder_sizes.items() if v <= 100000])}')
