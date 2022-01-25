import pathlib

bounds = []

def load_txt(filename):
    with open(pathlib.Path(__file__).with_name(filename))as file:
        line = file.readline()
        parts = line.split(' ')
        for part in parts:
            if part[0] == 'x' or part[0] == 'y':
                num1, num2 = part.split('..')
                num1 = num1[len('x='):]
                if part[0] == 'x':
                    num2 = num2[:-1]
                bounds.append(int(num1))
                bounds.append(int(num2))

def part1_solution():
    y_min = bounds[2]
    #since when y=0 both times the velocity must be the same, the largest change in a single step
    #is defined by the velocity_at_0 + 1 = initial_velocity + 1, and setting it equal to the y_min.
    largest_delta_y = abs(y_min) - 1
    return largest_delta_y * (largest_delta_y + 1) // 2
    
def part2_solution():
    y_min = bounds[2]
    largest_delta_y = abs(y_min) - 1
    vy_max = largest_delta_y 

    #verifier
    t_where_y_in_target = []
    
load_txt('input.txt')
print(part1_solution())