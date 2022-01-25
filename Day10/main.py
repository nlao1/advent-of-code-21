rows = []
def load_txt(filename: str) -> None:
    with open(filename) as file:
        for line in file:
            rows.append(line.strip())

illegal_point_values = {')': 3, ']': 57, '}': 1197, '>': 25137}
opening = {'(', '[', '{', '<'}
closing = {')', ']', '}', '>'}
opening_to_closing_dict = {'(': ')', '[': ']', '{': '}', '<': '>'}
closing_to_opening_dict = {')': '(', ']': '[', '}': '{', '>': '<'}

def part1_solution():
    stack = []
    score = 0
    for row in rows:
        for char in row:
            if char in opening:
                stack.append(char)
            elif char in closing:
                if closing_to_opening_dict[char] != stack[-1]:
                    score += illegal_point_values[char]
                    break
                else:
                    stack.pop() 
            else:
                raise ValueError
    print('part 1:', score)

def part2_solution():
    incomplete_scores = []
    for row in rows:
        stack = []
        for char in row:
            if char in opening:
                stack.append(char)
            elif char in closing:
                if closing_to_opening_dict[char] != stack[-1]:
                    stack.clear()
                    break
                else:
                    stack.pop()
            else:
                raise ValueError
        else:
            #now we know the line is incomplete
            curr_score = 0
            added_chars = []
            while len(stack) > 0:
                char = stack.pop()
                closing_char = opening_to_closing_dict[char]
                added_chars.append(closing_char)
                curr_score *= 5
                if closing_char == ']':
                    curr_score += 2
                elif closing_char == ')':
                    curr_score += 1
                elif closing_char == '}':
                    curr_score += 3
                elif closing_char == '>':
                    curr_score += 4
                else:
                    raise ValueError
            incomplete_scores.append(curr_score)
    incomplete_scores.sort()
    print('part 2:', incomplete_scores[len(incomplete_scores)//2])
    
load_txt('input.txt')
part1_solution()
part2_solution()