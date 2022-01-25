from typing import List

data_table = []
data_items_list = []
def load_data(filename):
    with open(filename) as file:
        num_cols_assgn = False
        for line in file:
            if not num_cols_assgn:
                num_cols = len(line) if line[-1] != '\n' else len(line) - 1
                for _ in range(num_cols):
                    data_table.append([])
                num_cols_assgn = True
            item = []
            for i in range(num_cols):
                data_table[i].append(int(line[i]))
                item.append(int(line[i]))
            data_items_list.append(item)

def part1_solution():
    gamma = [max(set(data_table[i]), key=data_table[i].count) for i in range(len(data_table))] 
    epsilon = [min(set(data_table[i]), key=data_table[i].count) for i in range(len(data_table))]
    print(bin_to_int(gamma) * bin_to_int(epsilon))

def part2_solution():
    #oxygen_ref
    oxygen_ref = [0 if data_table[i].count(0) > data_table[i].count(1) else 1 for i in range(len(data_table))]
    data_items_copy = [[i for i in row] for row in data_items_list]
    for i in range(len(data_items_copy[0])):
        data_items_copy = list(filter(lambda x: x[i] == oxygen_ref[i], data_items_copy))
        if len(data_items_copy) == 1:
            break
        oxygen_ref = [0 if [data_items_copy[j][i] for j in range(len(data_items_copy))].count(0) > [data_items_copy[j][i] for j in range(len(data_items_copy))].count(1) else 1 for i in range(len(data_items_copy[0]))]
    oxygen = data_items_copy[0]

    #co2
    co2_ref = [1 if data_table[i].count(1) < data_table[i].count(0) else 0 for i in range(len(data_table))]
    data_items_copy = [[i for i in row] for row in data_items_list]
    for i in range(len(data_items_copy[0])):
        data_items_copy = list(filter(lambda x: x[i] == co2_ref[i], data_items_copy))
        if len(data_items_copy) == 1:
            break
        co2_ref = [1 if [data_items_copy[j][i] for j in range(len(data_items_copy))].count(1) < [data_items_copy[j][i] for j in range(len(data_items_copy))].count(0) else 0 for i in range(len(data_items_copy[0]))]
    co2 = data_items_copy[0]
    print(bin_to_int(oxygen) * bin_to_int(co2))


def bin_to_int(lst : List[int]) -> int:
    result = 0
    for i in range(len(lst)):
        result *= 2 
        result += lst[i]
    return result

load_data('input.txt')
# part1_solution()
part2_solution()
