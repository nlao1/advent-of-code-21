import numpy
crabs = []
def load_txt(filename):
    with open(filename) as file:
        line = file.readline()
        for elt in line.split(','):
            crabs.append(int(elt))

def part1_solution(): #naive
    min_dist = sum(crabs)
    for point in range(min(crabs), max(crabs)):
        dist_sum = sum(abs(crab - point) for crab in crabs)
        min_dist = dist_sum if dist_sum < min_dist else min_dist
    print(min_dist)

def part2_solution():
    min_dist = sum(crab ** 2 for crab in crabs)
    for point in range(min(crabs), max(crabs)):
        dist_sum = 0
        for crab in crabs:
            abs_dist = abs(crab-point)
            dist_sum += (abs_dist) * (abs_dist + 1)/2
        min_dist = dist_sum if dist_sum < min_dist else min_dist
    print(min_dist)
load_txt('input.txt')
part1_solution()
part2_solution()