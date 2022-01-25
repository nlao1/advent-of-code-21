from typing import List

paper = []
folds = []
def load_txt(filename):
    with open(filename) as file:
        coords_list = []
        for line in file:
            if str.isnumeric(line[0]):
                x, y = map(lambda elt: int(elt), line.strip().split(','))
                coords_list.append((x,y))
            elif line[0] == 'f':
                fold, along, fold_line = line.strip().split(' ')
                axis, coord = fold_line.split('=')
                coord = int(coord)
                folds.append((axis, coord))
    max_x = max(map(lambda tuple: tuple[0], coords_list))
    max_y = max(map(lambda tuple: tuple[1], coords_list))
    temp_paper = [['.' for _ in range(max_x+1)] for _ in range(max_y+1)]
    paper.extend(temp_paper)
    for coord in coords_list:
        paper[coord[1]][coord[0]] = '#'
def part1_solution(end_index) -> List[List[str]]:
    prev_paper = paper
    for fold in folds[:end_index]:
        width = len(prev_paper[0])
        height = len(prev_paper)
        axis, coord = fold
        new_paper = []
        if axis == 'x': #fold left
            new_paper.extend([row[:coord] for row in prev_paper])
            for col in range(coord+1, width):
                col_in_new = coord - col #0 distance means right next to line
                for row in range(height):
                    new_paper[row][col_in_new] = '#' if prev_paper[row][col] == '#' or new_paper[row][col_in_new] == '#' else '.'
        elif axis == 'y': #fold up
            new_paper.extend([[i for i in row] for row in prev_paper[:coord]])
            for row in range(coord+1, height):
                row_in_new = coord - row #0 distance means right next to line
                for col in range(width):
                    new_paper[row_in_new][col] = '#' if prev_paper[row][col] == '#' or new_paper[row_in_new][col] == '#' else '.'   
        prev_paper = new_paper  
    print(sum(row.count('#') for row in new_paper))  
    return new_paper
def part2_solution(): #part 1 essentially
    completely_folded_paper = part1_solution(len(folds))
    print(matrix_to_str(completely_folded_paper))
def matrix_to_str(m: List[List]) -> str:
    output = ''
    for row in m:
        row_str = ''
        for elt in row:
            row_str += elt
        row_str+='\n'
        output+=row_str
    return output
load_txt('input.txt')
part1_solution(1)
part2_solution()
