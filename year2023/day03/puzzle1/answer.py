import os

digits = [str(x) for x in range(0, 10)]
ans = 0

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]

    for line_no in range(0, len(lines)):
        print(f"Working on line: {line_no}")
        line = lines[line_no]
        left_pointer = 0

        while left_pointer < len(line):
            if line[left_pointer] in digits:
                # Obtain the full number
                right_pointer = left_pointer
                while right_pointer + 1 <= len(line) - 1 and line[right_pointer + 1] in digits:
                    right_pointer += 1
                value = int(line[left_pointer : right_pointer + 1])

                # Check around the number string and see if any non-digits
                points_to_check = []
                points_to_check.extend([(line_no + shift, left_pointer - 1) for shift in [-1, 0, 1] ])
                points_to_check.extend([(line_no + shift, right_pointer + 1) for shift in [-1, 0, 1] ])
                points_to_check.extend([(line_no + 1, left_pointer + shift) for shift in range(0, right_pointer - left_pointer + 1) ])
                points_to_check.extend([(line_no - 1, left_pointer + shift) for shift in range(0, right_pointer - left_pointer + 1) ])
                
                for r, c in points_to_check:
                    if r < 0 or c < 0 or r >= len(lines) or c >= len(line):
                        # Not in grid
                        continue
                    if lines[r][c] not in digits and lines[r][c] != '.':
                        # Valid
                        print(f'{value} is adjacent to {lines[r][c]}')
                        ans += value
                        break

                left_pointer = right_pointer
            left_pointer += 1

print(ans)