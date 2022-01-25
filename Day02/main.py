data = []


def load_txt(filename):
    with open(filename) as file:
        for line in file:
            line_list = line.split(" ")
            data.append((line_list[0], int(line_list[1])))


def part1_solution():
    hor_pos = 0
    depth = 0
    for insn in data:
        dir = insn[0]
        amt = insn[1]
        if dir == "forward":
            hor_pos += amt
        elif dir == "down":
            depth += amt
        else:
            depth -= amt
    print("part1", hor_pos * depth)


def part2_solution():
    hor_pos = 0
    depth = 0
    aim = 0
    for insn in data:
        dir = insn[0]
        amt = insn[1]
        if dir == "forward":
            hor_pos += amt
            depth += aim * amt
        elif dir == "down":
            aim += amt
        else:
            aim -= amt
    print("part2", hor_pos * depth)


load_txt("input.txt")
part1_solution()
part2_solution()
