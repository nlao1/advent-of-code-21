from typing import Tuple

pairs_list = []
matrix = []

def load_txt(filename):
    with open(filename) as file:
        for line in file:
            pair1, pair2 = line.split(' -> ')
            comps1 = pair1.split(',')
            comps2 = pair2.split(',')
            pairs_list.append(
                [
                    (int(comps1[0]), int(comps1[1])), 
                    (int(comps2[0]), int(comps2[1]))
                ]
            )

def find_matrix_dims():
    max_x = max(max(pair[0][0], pair[1][0]) for pair in pairs_list)
    max_y = max(max(pair[0][1], pair[1][0]) for pair in pairs_list)
    return [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)] 

def part1_solution():
    for pair1, pair2 in pairs_list:
        if pair1[0] == pair2[0]: #vertical
            for i in range(pair1[1], pair2[1] - 1, -1) if pair1[1] > pair2[1] else range(pair1[1], pair2[1] + 1):
                matrix[i][pair1[0]] += 1 
        elif pair1[1] == pair2[1]: #horizontal
            for j in range(pair1[0], pair2[0] - 1, -1) if pair1[0] > pair2[0] else range(pair1[0], pair2[0] + 1):
                matrix[pair1[1]][j] += 1
    count = sum([(1 if matrix[i][j] >=2 else 0) for i in range(len(matrix)) for j in range(len(matrix[i]))])
    print(count)

def part2_solution():
    for pair1, pair2 in pairs_list:
        if pair1[0] == pair2[0]: #vertical
            for i in inclusive_signed_range(pair1, pair2):
                matrix[i][pair1[0]] += 1 
        elif pair1[1] == pair2[1]: #horizontal
            for j in inclusive_signed_range(pair1, pair2):
                matrix[pair1[1]][j] += 1
        else: #diagonal
            for (x,y) in inclusive_signed_range(pair1, pair2):
                matrix[y][x] += 1
    count = sum([(1 if matrix[i][j] >=2 else 0) for i in range(len(matrix)) for j in range(len(matrix[i]))])
    print(count)

def inclusive_signed_range(pair1 : Tuple[int, int], pair2 : Tuple[int, int]):
    if pair1[0] == pair2[0]:
        return range(pair1[1], pair2[1] - 1, -1) if pair1[1] > pair2[1] else range(pair1[1], pair2[1] + 1)
    elif pair1[1] == pair2[1]:
        return range(pair1[0], pair2[0] - 1, -1) if pair1[0] > pair2[0] else range(pair1[0], pair2[0] + 1)
    else:
        x = pair1[0]
        y = pair1[1]
        end_x = pair2[0]
        end_y = pair2[1]
        x_dir = -1 if x > end_x else 1
        y_dir = -1 if y > end_y else 1
        while x != end_x and y != end_y:
            yield (x,y)
            x += x_dir 
            y += y_dir
        yield (end_x, end_y)

load_txt('input.txt')
matrix = find_matrix_dims()
part1_solution()
part2_solution()