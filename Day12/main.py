from collections import defaultdict
from typing import List, Set

graph: dict = defaultdict(set) 
big = set()
small = set()
def load_txt(filename):
    with open(filename) as file:
        for line in file:
            vertices = line.strip().split('-')
            for vertex in vertices:
                if vertex[0].isupper():
                    big.add(vertex)
                else:
                    small.add(vertex)
            graph[vertices[0]].add(vertices[1])
            graph[vertices[1]].add(vertices[0])
def part1_solution():
    paths: Set[List[str]] = set()
    dfs_part_1(paths, ['start'], 'start')
    #will probably use dfs
    print(len(paths))

def dfs_part_1(paths: Set[List[str]], path_so_far: List[str], vertex: str) -> None:
    if vertex == 'end':
        paths.add(list_to_path_str(path_so_far))
    else:
        for neighbor in graph[vertex]:
            if neighbor in path_so_far and neighbor in big or neighbor not in path_so_far:
                dfs_part_1(paths, path_so_far.copy()+[neighbor], neighbor)

def part2_solution():
    paths: Set[List[str]] = set()
    dfs_part_2(paths, ['start'], 'start')
    #will probably use dfs
    print(len(paths))

def dfs_part_2(paths: Set[List[str]], path_so_far: List[str], vertex: str) -> None:
    if vertex == 'end':
        paths.add(list_to_path_str(path_so_far))
    else:
        for neighbor in graph[vertex]:
            new_path = path_so_far.copy()+[neighbor]
            only_one_small_cave_repeated = True
            repeated_vertex = None
            for vertex in small:
                if new_path.count(vertex) == 2:
                    if repeated_vertex is None:
                        repeated_vertex = vertex
                    else:
                        only_one_small_cave_repeated = False
                elif new_path.count(vertex) > 2:
                    only_one_small_cave_repeated = False
            if neighbor in big or neighbor in small and only_one_small_cave_repeated and repeated_vertex not in {'start', 'end'}:
                dfs_part_2(paths, new_path, neighbor)

def list_to_path_str(l: List) -> str:
    output_str = ''
    for item in l:
        if item == l[0]:
            output_str += str(item)
        else:
            output_str += ',' + str(item)
    return output_str
load_txt('input.txt')
part1_solution()
part2_solution()