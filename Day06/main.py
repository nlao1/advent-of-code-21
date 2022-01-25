from collections import defaultdict
from typing import DefaultDict


class Solver:
    def __init__(self):
        self.fish_list = []
    def load_txt(self, filename):
        with open(filename) as file:
            line = file.readline()
            fish = line.split(',')
            self.fish_list = [int(i) for i in fish]
    def simulate(self, days: int):
        for day in range(1, days + 1):
            generate_counter = 0
            for i in range(len(self.fish_list)):
                if self.fish_list[i] == 0:
                    self.fish_list[i] = 6
                    generate_counter += 1
                else:
                    self.fish_list[i] -= 1
            for _ in range(generate_counter):
                self.fish_list.append(8)
            # print(f'after {day} days: ', self.fish_list)

    def simulate_faster(self, days: int):
        fish_dict = defaultdict(lambda: 0)
        for fish in sorted(self.fish_list):
            fish_dict[fish] += 1
        #simulate
        for day in range(1, days + 1):
            new_generate = fish_dict[0]
            for i in range(0, 8):
                fish_dict[i] = fish_dict[i+1]
            fish_dict[8] = new_generate
            fish_dict[6] += new_generate
        print(sum(fish_dict.values()))
if __name__ == "__main__":
    solver = Solver()
    solver.load_txt('input.txt')
    solver.simulate_faster(256)
