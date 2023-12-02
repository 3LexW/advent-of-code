ans = 0

# List out digits from 1 to nine
letter_digits_dict = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
}
number_digits = [str(i) for i in range(0, 10)]
letter_digits = [i for i in letter_digits_dict.keys()]

with open("./input.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    # print(line)

    # Left digit
    for i in range(0, len(line)):
        left_digit = [x for x in number_digits if line[i : len(line)].startswith(x)] + \
            [letter_digits_dict[x] for x in letter_digits if line[i : len(line)].startswith(x)]

        if len(left_digit) > 0:
            left_digit = left_digit[0]
            break
    
    # Right digit
    for i in range(len(line), 0, -1):
        right_digit = \
            [x for x in number_digits if line[0:i].endswith(x)] + \
            [letter_digits_dict[x] for x in letter_digits if line[0:i].endswith(x)]
        
        if len(right_digit) > 0:
            right_digit = right_digit[0]
            break

    ans += int(f'{left_digit}{right_digit}')

print(ans)