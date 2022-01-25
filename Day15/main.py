from collections import defaultdict, deque
import math
from typing import Dict, List, Tuple
from queue import PriorityQueue

matrix = []
vertex_to_weight = {}
def load_txt(filename):
    with open(filename) as file:
        for line in file:
            line_as_lst = list(map(lambda x: int(x), list(line.strip())))
            matrix.append(line_as_lst)

def construct_graph(matrix: List[List[int]]) -> Dict[int, Dict[int, int]]: #dict in case edge weights added later
    graph = defaultdict(dict)
    width = len(matrix[0])
    height = len(matrix)
    for row in range(height):
        for col in range(width):
            curr_vertex = coords_to_index(width, row, col)
            if row - 1 >= 0:
                up = coords_to_index(width, row - 1, col)
                graph[curr_vertex][up] = matrix[row - 1][col]
            if row + 1 < height:
                down = coords_to_index(width, row + 1, col)
                graph[curr_vertex][down] = matrix[row+1][col]
            if col - 1 >= 0:
                left = coords_to_index(width, row, col - 1)
                graph[curr_vertex][left] = matrix[row][col-1]
            if col + 1 < width:
                right = coords_to_index(width, row, col + 1)
                graph[curr_vertex][right] = matrix[row][col+1]
            vertex_to_weight[coords_to_index(width, row, col)] = matrix[row][col]
    return graph

def part1_solution(graph: Dict[int, Dict[int, int]]) -> None:
    distances = {v: float('inf') for v in graph}
    parent = [None for v in graph]
    visited = set()
    distances[0] = 0
    pq = PriorityQueue()
    pq.put((0, 0))

    while not pq.empty():
        dist, curr_vertex = pq.get() 
        visited.add(curr_vertex)
        for neighbor in graph[curr_vertex]:
            distance = graph[curr_vertex][neighbor]
            if neighbor not in visited:
                old_cost = distances[neighbor]
                new_cost = distances[curr_vertex] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, neighbor))
                    parent[neighbor] = curr_vertex
                    distances[neighbor] = new_cost
    dest = max(graph.keys())
    print(distances[dest])

def construct_enlarged_graph(matrix: List[List[int]]):
    vertex_to_weight = {}
    #construct a 25x size dict
    #transition edges can be done with math??
    graph = defaultdict(dict)
    width = len(matrix[0])
    height = len(matrix)
    LARGE_GRAPH_WIDTH = 5
    LARGE_GRAPH_HEIGHT = 5
    for i in range(LARGE_GRAPH_WIDTH):
        for j in range(LARGE_GRAPH_HEIGHT):
            for row in range(height):
                for col in range(width):
                    curr_vertex, curr_weight = large_graph_index_value(width, height, row, col, i, j)
                    if i > 0 or row - 1 >= 0:
                        up, up_weight = large_graph_index_value(width, height, row - 1, col, i, j)
                        graph[curr_vertex][up] = up_weight
                    if row + 1 < height or i + 1< LARGE_GRAPH_HEIGHT:
                        down, down_weight = large_graph_index_value(width, height, row + 1, col, i, j)
                        graph[curr_vertex][down] = down_weight
                    if j > 0 or col - 1 >= 0:
                        left, left_weight = large_graph_index_value(width, height, row, col - 1, i, j)
                        graph[curr_vertex][left] = left_weight
                    if col + 1 < width or j + 1 < LARGE_GRAPH_WIDTH:
                        right, right_weight = large_graph_index_value(width, height, row, col + 1, i , j)
                        graph[curr_vertex][right] = right_weight
                    vertex_to_weight[curr_vertex] = curr_weight
    return graph

def part2_solution() -> None:
    graph = construct_enlarged_graph(matrix)
    #do i have the time to construct the entire graph.. 
    # yes!
    part1_solution(construct_enlarged_graph(matrix))

def coords_to_index(width: int, row: int, col: int) -> int:
    return width * row + col

def large_graph_index_value(width, height, row, col, i, j) -> Tuple[int, int]:
    """
    coords defined as `[`
        `[(0...w*h-1),(w*h*1...w*h*2-1),..., (w*h*4...w*h*5-1)]`\n
        `[(w*h*5...), ...]`\n
        `...`
    `]`
    """
    if row == -1:
        return large_graph_index_value(width, height, height - 1, col, i - 1, j)
    elif col == -1:
        return large_graph_index_value(width, height, row, width - 1, i, j - 1)
    elif row == height:
        return large_graph_index_value(width, height, 0, col, i + 1, j)
    elif col == width:
        return large_graph_index_value(width, height, row, 0, i, j + 1)
    else:
        weight = (matrix[row][col] + i + j) % 9 
        return ((i * 5 + j) * width * height + coords_to_index(width, row, col), 9 if weight % 9 == 0 else weight) 
load_txt('input.txt')
graph = construct_graph(matrix)
part1_solution(graph)
part2_solution()