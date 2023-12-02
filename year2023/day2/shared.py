import itertools

def split_line(line):
    game_id = int(line.split(": ")[0].split(" ")[-1])

    sets = line.strip().split(": ")[-1].split("; ")
    draws = list(itertools.chain.from_iterable([x.split(", ") for x in sets]))

    return game_id, draws