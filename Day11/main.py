from collections import deque
from typing import List

data = []
def load_txt(filename):
    with open(filename) as file:
        for line in file:
            stripped = line.strip()
            line_list = [int(i) for i in stripped]
            data.append(line_list)
        
def part1_solution(num_steps):
    matrix = [[i for i in row] for row in data] #copy it first
    flashes = 0
    for _ in range(num_steps):
        flash_coords = deque() #stores (row, col) tuples
        flashed = [[False for _ in row] for row in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j]+=1
                if matrix[i][j] > 9:
                    flash_coords.append((i,j))
        while flash_coords:
            flash_row, flash_col = flash_coords.popleft()
            if not flashed[flash_row][flash_col]:
                flashed[flash_row][flash_col] = True
                flashes+=1
                for y in range(flash_row - 1, flash_row + 2, 1):
                    for x in range(flash_col - 1, flash_col + 2, 1):
                        if x >= 0 and y >= 0 and x < len(matrix[0]) and y < len(matrix) and (x != flash_col or y != flash_row):
                            matrix[y][x] += 1
                            if matrix[y][x] > 9:
                                flash_coords.append((y, x))
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if flashed[i][j]:
                    matrix[i][j] = 0
    print('part 1: flashed', flashes, 'times') 
def part2_solution(filename) -> int:
    matrix = [[i for i in row] for row in data]
    flashes = 0
    step = 0
    while True:
        step+=1
        flash_coords = deque() #stores (row, col) tuples
        flashed = [[False for _ in row] for row in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j]+=1
                if matrix[i][j] > 9:
                    flash_coords.append((i,j))
        while flash_coords:
            flash_row, flash_col = flash_coords.popleft()
            if not flashed[flash_row][flash_col]:
                flashed[flash_row][flash_col] = True
                flashes+=1
                for y in range(flash_row - 1, flash_row + 2, 1):
                    for x in range(flash_col - 1, flash_col + 2, 1):
                        if x >= 0 and y >= 0 and x < len(matrix[0]) and y < len(matrix) and (x != flash_col or y != flash_row):
                            matrix[y][x] += 1
                            if matrix[y][x] > 9:
                                flash_coords.append((y, x))

        all_flashed = True
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if flashed[i][j]:
                    matrix[i][j] = 0
                else:
                    all_flashed = False
        if all_flashed:
            break
    print('part 2: all flashed at', step, 'step') 

tested_file = 'input.txt'
load_txt(tested_file)
part1_solution(100)
part2_solution(tested_file)
