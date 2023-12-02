ans = 0
number_digits = [str(i) for i in range(0, 10)]

with open('input.txt', 'r') as file:
    lines = file.readlines()

# For each line, combine the first number digit and the last number digit and form a two letter number
for line in lines:
    left_pointer = 0
    right_pointer = len(line) - 1

    while line[left_pointer:left_pointer + 1] not in number_digits:
        left_pointer += 1

    while line[right_pointer:right_pointer + 1] not in number_digits:
        right_pointer -= 1
    
    ans += int(f'{line[left_pointer]}{line[right_pointer]}')

print(ans)