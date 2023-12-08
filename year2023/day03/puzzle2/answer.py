from functools import reduce
import os
import itertools

digits = [str(x) for x in range(0, 10)]
shifts = list(itertools.product([0, 1, -1], [0, 1, -1]))
shifts.remove((0, 0))
checked_pointer = []

ans = 0

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]

    for line_no in range(0, len(lines)):
        print(f"Working on line: {line_no + 1}")
        line = lines[line_no]
        pointer = 0

        while pointer < len(line):
            if lines[line_no][pointer] == '*':
                symbol = lines[line_no][pointer]
                print(f"Found symbol: {symbol}")
                values = []
                for r_shift, c_shift in shifts:
                    if (
                        line_no + r_shift < 0
                        or pointer + c_shift < 0
                        or line_no + r_shift >= len(lines)
                        or pointer + c_shift >= len(line)
                    ):
                        continue

                    if (
                        lines[line_no + r_shift][pointer + c_shift] in digits
                        and (line_no + r_shift, pointer + c_shift)
                        not in checked_pointer
                    ):
                        checked_pointer.append((line_no + r_shift, pointer + c_shift))

                        # Obtain the full digit
                        left = pointer + c_shift
                        while left > 0 and lines[line_no + r_shift][left - 1] in digits:
                            left -= 1
                            checked_pointer.append((line_no + r_shift, left))
                        right = pointer + c_shift
                        while (
                            right < len(line) - 1
                            and lines[line_no + r_shift][right + 1] in digits
                        ):
                            right += 1
                            checked_pointer.append((line_no + r_shift, right))
                        values.append(int(lines[line_no + r_shift][left : right + 1]))

                print(values)
                if symbol == "*":
                    ans += reduce(lambda a, b: a * b, values) if len(values) == 2 else 0
                else:
                    ans += reduce(lambda a, b: a + b, values)

            pointer += 1


print(ans)
