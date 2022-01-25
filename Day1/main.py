from collections import deque

from numpy import datetime_as_string
from numpy.lib.npyio import load

data = []


def load_txt(filename):
    with open(filename) as file:
        for line in file:
            data.append(int(line))


def part1_solution():
    prev = -1
    counter = 0
    for num in data:
        if prev == -1:
            prev = num
        else:
            if num > prev:
                counter += 1
        prev = num
    else:
        print(counter)


def part2_solution():
    window_sum = sum(data[:3])
    prev_sum = window_sum
    counter = 0
    for i in range(3, len(data)):
        window_sum += (-data[i - 3]) + data[i]
        if window_sum > prev_sum:
            counter += 1
        prev_sum = window_sum
    else:
        print(counter)


if __name__ == "__main__":
    load_txt("input.txt")
    part1_solution()
    part2_solution()
