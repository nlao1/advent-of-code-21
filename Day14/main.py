from typing import List, Dict
import functools
from collections import defaultdict

template = []
insertion_rules = {}
def load_txt(filename):
    with open(filename) as file:
        template_str = file.readline()
        for char in template_str.strip():
            template.append(char)
        file.readline() #empty
        for line in file:
            input, output = line.strip().split(' -> ')
            insertion_rules[input] = output

def part1_solution(steps):
    init_polymer = template
    polymer = init_polymer
    for step in range(steps):
        temp_polymer = []
        for i in range(len(polymer) - 1):
            pair = polymer[i:i+2]
            input = polymer_to_str(pair)
            if i == 0:
                temp_polymer.append(pair[0])
            temp_polymer.append(insertion_rules[input])
            temp_polymer.append(pair[1]) 
        polymer = temp_polymer
    most_common = max(polymer.count(x) for x in polymer)
    least_common = min(polymer.count(x) for x in polymer)
    print(most_common - least_common)

def part2_solution(steps):
    init_polymer = defaultdict(lambda: 0)
    for i in range(len(template) - 1):
        pair = polymer_to_str(template[i:i+2])
        init_polymer[pair] += 1
    prev_polymer = init_polymer
    for step in range(steps):
        temp_polymer = defaultdict(lambda: 0)
        for pair in prev_polymer:
            count = prev_polymer[pair]
            output = insertion_rules[pair]
            temp_polymer[pair[0] + output] += count
            temp_polymer[output + pair[1]] += count
        prev_polymer = temp_polymer
    counts = count_letters(prev_polymer)
    print(max(counts.values()) - min(counts.values()))
def count_letters(polymer: Dict) -> Dict[str, int]:
    first_letter = template[0]
    last_letter = template[-1]
    counts = defaultdict(lambda: 0)
    for key, value in polymer.items():
        char1 = key[0]
        char2 = key[1]
        counts[char1] += value
        counts[char2] += value
    for key in counts:
        if key == first_letter or key == last_letter:
            counts[key] = (counts[key] - 1) // 2 + 1
        else:
            counts[key] //= 2
    return counts
def polymer_to_str(l: List[str]):
    output = ''
    return functools.reduce(lambda acc, x: acc + x, l)
load_txt('input.txt')
part1_solution(10)
part2_solution(40)