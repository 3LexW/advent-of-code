import os
import re

tree = {}
wire = {}
assignments = []

with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    for line in [x.strip() for x in f.readlines()]:
        if ":" in line:
            tree[line.split(": ")[0]] = (
                int(line.split(": ")[1]) == 1,
                None,
                None,
                None,
            )
        if "->" in line:
            a, operator, b, to_value = re.findall(
                r"(.*) (OR|AND|XOR) (.*) -> (.*)", line
            )[0]
            wire[to_value] = (a, operator, b)
            assignments.append((a, operator, b, to_value))

while assignments:
    a, operator, b, to_value = assignments.pop(0)
    if (a in tree and b in tree) is False:
        assignments.append((a, operator, b, to_value))
        continue
    match operator:
        # insert (value, a, operator, b)
        case "OR":
            tree[to_value] = (tree[a][0] or tree[b][0], a, operator, b)
        case "XOR":
            tree[to_value] = (tree[a][0] != tree[b][0], a, operator, b)
        case "AND":
            tree[to_value] = (tree[a][0] and tree[b][0], a, operator, b)


def get_value(prefix: str):
    ans = 0
    for _, value in sorted(
        {key: value for key, value in tree.items() if key.startswith(prefix)}.items(),
        reverse=True,
    ):
        ans = ans << 1
        ans += int(value[0])
    return ans


print(f"Puzzle 1: {get_value("z")}")


def print_tree(goal, depth=0):
    if goal not in wire:
        print(f"{'.' * depth}{goal}")
        return
    x, operator, y = wire[goal]
    print(f"{'.' * depth}{goal} ({operator})")
    print_tree(x, depth + 1)
    print_tree(y, depth + 1)


def check_z(goal, bit):
    print(f"Check z on {goal}, bit: {bit}")
    x, operator, y = wire[goal]
    if operator != "XOR":
        return False
    if bit == 0:
        return sorted([x, y]) == ["x00", "y00"]

    # Otherwise, have to check carry and base
    return (check_carry(x, bit - 1) and check_intermediate(y, bit)) or (
        check_carry(y, bit - 1) and check_intermediate(x, bit)
    )


def check_carry(goal, bit):
    print(f"Check carry on {goal}, bit: {bit}")
    try:
        x, operator, y = wire[goal]
    except Exception:
        return False
    if bit == 0:
        return sorted([x, y]) == ["x00", "y00"] and operator == "AND"

    if operator != "OR":
        return False
    return (check_intermediate_carry(x, bit) and check_direct_carry(y, bit)) or (
        check_intermediate_carry(y, bit) and check_direct_carry(x, bit)
    )


def check_intermediate(goal, bit):
    print(f"Check intermediate on {goal}, bit: {bit}")
    try:
        x, operator, y = wire[goal]
    except Exception:
        return False
    if operator != "XOR":
        return False
    return sorted([x, y]) == [f"x{bit:02}", f"y{bit:02}"]


def check_direct_carry(goal, bit):
    print(f"Check direct carry on {goal}, bit: {bit}")
    try:
        x, operator, y = wire[goal]
    except Exception:
        return False
    if operator != "AND":
        return False
    return sorted([x, y]) == [f"x{bit:02}", f"y{bit:02}"]


def check_intermediate_carry(goal, bit):
    print(f"Check intermediate carry on {goal}, bit: {bit}")
    try:
        x, operator, y = wire[goal]
    except Exception:
        return False
    if operator != "AND":
        return False
    return (check_carry(x, bit - 1) and check_intermediate(y, bit)) or (
        check_carry(y, bit - 1) and check_intermediate(x, bit)
    )


for i in range(0, 45):
    if not check_z(f"z{i:02}", i):
        print_tree(f"z{i:02}")
        exit()
    else:
        print()

### Manual checks

# First failed on z06, which is not XOR
# Check x06 XOR y06 is gbp
# Check gbp XOR scp is vwr
# Swap z06 and vwr

# Second failed on z11, which is not XOR
# Check x11 XOR y11 is sqv
# Check xqv XOR frp is tqm
# Swap z11 and tqm

# Third failed on z16, which is not XOR
# Check x16 XOR y16 is vgv
# Check vgv XOR hpt is kfs
# Swap z16 and kfs

# Fourth failed on z36, failed on intermediate side (hcm = x36 AND y36)
# Check x36 XOR y36 is gfv
# Swap gfv and hcm

# Done

p2 = ["z06", "vwr", "z11", "tqm", "z16", "kfs", "gfv", "hcm"]
print(",".join(sorted(p2)))
