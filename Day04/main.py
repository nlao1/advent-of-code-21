from typing import List

data = []
num_seq = []
def load_txt(filename):
    with open(filename) as file:
        first_line = file.readline()
        first_line_list = first_line.split(',')
        for num in first_line_list:
            num_seq.append(int(num))
        file.readline()
        board = []
        for line in file:
            if line == '\n':
                data.append(board)
                board = []
            else: 
                nums = list(filter(lambda x: x != '', line.split(' ')))
                board.append([int(num) for num in nums])
        else:
            data.append(board)
def check_done(board: List[List[int]]) -> bool:
    for row in board:
        for elt in row:
            if elt is not None:
                break
        else: 
            return True
    
    for j in range(len(board[0])):
        for i in range(len(board)):
            if board[i][j] is not None:
                break
        else:
            return True
    return False

def part1_solution():
    for i in range(len(num_seq)):
        called = num_seq[i]
        for board in data:
            for j in range(len(board)):
                for k in range(len(board[j])):
                    if board[j][k] == called:
                        board[j][k] = None
            if check_done(board):
                print(sum(sum(list(filter(lambda x: x is not None, board[l]))) for l in range(len(board))) * called)
                return None

def part2_solution():
    wins = [False for _ in range(len(data))]
    for i in range(len(num_seq)):
        called = num_seq[i]
        for board_id, board in enumerate(data):
            if not wins[board_id]:
                for j in range(len(board)):
                    for k in range(len(board[j])):
                        if board[j][k] == called:
                            board[j][k] = None
                if check_done(board):
                    wins[board_id] = True
                if wins.count(False) == 0:
                    print(sum(sum(list(filter(lambda x: x is not None, board[l]))) for l in range(len(board))) * called)

load_txt('input.txt')
part1_solution()
part2_solution()