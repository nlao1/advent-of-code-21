from typing import DefaultDict, Dict

decode_list = []
def load_txt(filename):
    with open(filename) as file:
        for line in file:
            comps = line.split('|')
            comps[0] = str.strip(comps[0])
            comps[1] = str.strip(comps[1])
            ref = comps[0].split(' ')
            output = comps[1].split(' ')
            decode_list.append((ref, output))

def part1_solution():
    count = 0
    for decode in decode_list:
        output = decode[1]
        for elt in output:
            if len(elt) in {2, 3, 4, 7}:
                count += 1
    print(count)

def part2_solution():
    a = 'a'; b = 'b'; c = 'c'; d = 'd'; e = 'e'; f = 'f'; g = 'g'
    result = 0
    ref_digit_display: Dict[int, set] = {0: {a,b,c,e,f,g}, 1: {c,f}, 2: {a,c,d,e,g}, 3:{a,c,d,f,g}, 4:{b,c,d,f},\
            5: {a,b,d,f,g}, 6: {a,b,d,e,f,g}, 7: {a,c,f}, 8: {a,b,c,d,e,f,g}, 9: {a,b,c,d,f,g}}
    char_to_numbers: Dict[str, set] = dict()
    for char in ref_digit_display[8]:
        temp_set = set()
        for key, value in ref_digit_display.items():
            if char in value:
                temp_set.add(key)
        char_to_numbers[char] = temp_set
    char_to_length = {} #for each char, map the dictionary of frequencies of lengths
    for key, val_set in char_to_numbers.items():
        for num in val_set:
            if key not in char_to_length:
                char_to_length[key] = dict()
            if num != 1 and num != 4 and num != 7:
                if len(ref_digit_display[num]) not in char_to_length[key]:
                    char_to_length[key][len(ref_digit_display[num])] = 1
                else:
                    char_to_length[key][len(ref_digit_display[num])] += 1
    for decode in decode_list:
        mapping = {char: {a,b,c,d,e,f,g} for char in {a,b,c,d,e,f,g}}
        ref = decode[0]
        output = decode[1]
        #for each segment, when does it turn on and what are the lengths when they do
        decode_char_to_length_dict = {char: dict() for char in ref_digit_display[8]}
        for elt in ref:
            if len(elt) == 2: #1
                for char in elt:
                    mapping[char].intersection_update(ref_digit_display[1])
            elif len(elt) == 3: #7
                for char in elt:
                    mapping[char].intersection_update(ref_digit_display[7])
            elif len(elt) == 4: #4
                for char in elt:
                    mapping[char].intersection_update(ref_digit_display[4])
            else:
                length = len(elt)
                for char in elt:
                    temp_dict = decode_char_to_length_dict[char]
                    if length not in temp_dict:
                        temp_dict[length] = 1
                    else:
                        temp_dict[length] += 1
        for decode_char, length_dict in decode_char_to_length_dict.items():
            for char, mapped in char_to_length.items():
                if decode_char in mapping and length_dict != mapped:
                    if char in mapping[decode_char]:
                        mapping[decode_char].remove(char)
        for char in mapping:
            for mapped_set in mapping.values():
                mapped_char = list(mapping[char])[0]
                if len(mapping[char]) == 1 and mapped_char in mapped_set and len(mapped_set) > 1:
                    mapped_set.remove(mapped_char)
        decoded_output = []
        for word in output:
            char_set = {list(mapping[char])[0] for char in word}
            for num, mapped_set in ref_digit_display.items():
                if char_set == mapped_set:
                    decoded_output.append(num)
        for i in range(3, -1, -1):
            result += 10 ** abs(3-i) * decoded_output[i]
    print(result)
load_txt('input.txt')
# part1_solution()
part2_solution()