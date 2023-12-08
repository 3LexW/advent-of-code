def get_score(letter: str):
    if len(letter) != 1:
        raise Exception("Letter should be one letter")
    if ord("a") <= ord(letter) <= ord("z"):
        return ord(letter) - ord("a") + 1
    if ord("A") <= ord(letter) <= ord("Z"):
        return ord(letter) - ord("A") + 27