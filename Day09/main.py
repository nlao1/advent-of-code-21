from typing import List
import heapq

matrix = []
def load_txt(filename):
    with open(filename) as file:
        for line in file:
            cleaned_list = list(line)[:-1] if line[-1] == '\n' else list(line)
            matrix.append([int(elt) for elt in cleaned_list])

def part1_solution():
    total_danger = 0
    height = len(matrix)
    width = len(matrix[0])
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            entry = matrix[row][col]
            if row - 1 >= 0 and matrix[row-1][col] <= entry or \
                row + 1 < height and matrix[row+1][col] <= entry or \
                col - 1 >= 0 and matrix[row][col-1] <= entry or \
                col + 1 < width and matrix[row][col+1] <= entry:
                continue
            else:
                total_danger += entry + 1
    print('part 1 solution:', total_danger)

def part2_solution():
    height = len(matrix)
    width = len(matrix[0])
    basin_size_heap = []
    heapq.heapify(basin_size_heap)
    matrix_copy = [[i for i in row] for row in matrix]

    for row in range(height):
        for col in range(width):
            entry = matrix[row][col]
            if row - 1 >= 0 and matrix[row-1][col] <= entry or \
                row + 1 < height and matrix[row+1][col] <= entry or \
                col - 1 >= 0 and matrix[row][col-1] <= entry or \
                col + 1 < width and matrix[row][col+1] <= entry:
                continue
            else:
                heapq.heappush(basin_size_heap, flood_fill(matrix_copy, row, col))
                if len(basin_size_heap) > 3:
                    heapq.heappop(basin_size_heap)
    #implement a floodfill from each low point to find the size of the basin that it's in
    print("part 2 solution:", basin_size_heap[0] * basin_size_heap[1] * basin_size_heap[2])

def flood_fill(matrix: List[List[int]], row: int, col: int) -> int:
    if row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0]) and matrix[row][col] != 9:
        matrix[row][col] = 9
        return 1 + flood_fill(matrix, row + 1, col) + flood_fill(matrix, row - 1, col) + flood_fill(matrix, row, col + 1) + flood_fill(matrix, row, col - 1)
    else:
        return 0
    
load_txt('input.txt')
part1_solution()
part2_solution()