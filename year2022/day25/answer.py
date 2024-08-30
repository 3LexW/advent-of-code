import os


def snafu_to_decimal(snafu: str):
    values = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}

    power = 0
    ans = 0

    for i in range(0, len(snafu)):
        ans += 5**power * values[snafu[len(snafu) - 1 - i]]
        power += 1

    return ans


def decimal_to_snafu(dec: int):
    array = []
    ans = ""

    while dec > 0:
        array.insert(0, dec % 5)
        dec //= 5

    for i in range(0, len(array)):
        match array[len(array) - 1 - i]:
            case 0:
                ans = f"0{ans}"
            case 1:
                ans = f"1{ans}"
            case 2:
                ans = f"2{ans}"
            case 3:
                if i != len(array) - 1:
                    ans = f"={ans}"
                    array[len(array) - i - 2] += 1
                else:
                    ans = f"1={ans}"
            case 4:
                if i != len(array) - 1:
                    ans = f"-{ans}"
                    array[len(array) - i - 2] += 1
                else:
                    ans = f"1-{ans}"
            case 5:
                if i != len(array) - 1:
                    ans = f"0{ans}"
                    array[len(array) - i - 2] += 1
                else:
                    ans = f"10{ans}"

    return ans


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    total = 0
    for line in f.readlines():
        total += snafu_to_decimal(line.strip())

    print(total)
    print(decimal_to_snafu(total))
