import os
import re

mappings = {}


def evaluate(x, m, a, s, code):
    global mappings

    if code not in mappings:
        raise Exception(f"Unknown code: {code}")

    for check in mappings[code].split(","):
        if ":" in check:
            print(f"Begin evaluation of {check.split(':')[0]}")
            expression = (
                check.split(":")[0]
                .replace("x", str(x))
                .replace("m", str(m))
                .replace("a", str(a))
                .replace("s", str(s))
            )
            if not eval(expression):
                print(f"Evaluation {expression} is False, move to next")
                continue
            else:
                result = check.split(":")[1]
                print(f"Evaluation successful, move to {result}")
                if check_result(result) != None:
                    return check_result(result)
                else:
                    return evaluate(x, m, a, s, result)
        else:
            print(f"Final review, go to {check}")
            if check_result(check) != None:
                return check_result(check)
            else:
                return evaluate(x, m, a, s, check)


def check_result(code: str):
    if code == "A":
        return True
    elif code == "R":
        return False
    return None


ans = 0

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    is_code = True
    for line in f.readlines():
        if len(line.strip()) == 0:
            is_code = False
            continue

        if is_code:
            code, rule = re.match(r"([a-z]+)\{(.*)\}", line.strip()).groups()
            mappings[code] = rule
        else:
            x, m, a, s = re.match(
                r"\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}", line.strip()
            ).groups()
            x, m, a, s = int(x), int(m), int(a), int(s)
            if evaluate(x, m, a, s, "in"):
                print("Successful, add value")
                ans += x + m + a + s
            print()

print(f"Puzzle 1: {ans}")
