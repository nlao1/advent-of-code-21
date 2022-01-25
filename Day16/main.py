from collections import deque
from os import read
from typing import Deque, Optional, List
import pathlib
from functools import reduce

binary_str = []


def load_txt(filename):
    with open(pathlib.Path(__file__).with_name(filename)) as file:
        line = file.readline()
        for char in line.strip():
            binary_rep = f"{int(char, base=16):0>4b}"
            for digit in binary_rep:
                binary_str.append(int(digit))


def part1_solution(bitstream: Deque[int], num_packets_to_read: Optional[int]):
    version_sum = 0
    num_packets_read = 0
    while (
        len(bitstream) > 10
        and num_packets_to_read is None
        or (num_packets_to_read is not None and num_packets_read < num_packets_to_read)
    ):
        num_packets_read += 1
        version = read_bits(bitstream, 3)
        version_sum += version
        type_id = read_bits(bitstream, 3)
        if type_id == 4:  # literal
            literal = 0
            zero_found = False
            while not zero_found:
                literal <<= 4
                zero_found = read_bits(bitstream, 1) == 0
                literal += read_bits(bitstream, 4)
            # literal can be retrieved here
        else:  # operator
            length_type_id = read_bits(bitstream, 1)
            if length_type_id == 0:
                total_length_subpackets = read_bits(bitstream, 15)
                version_sum += part1_solution(
                    deque([bitstream.popleft() for _ in range(total_length_subpackets)]), None
                )
            else:
                num_subpackets = read_bits(bitstream, 11)
                version_sum += part1_solution(bitstream, num_subpackets)
    return version_sum


def part2_solution(bitstream: Deque[int], num_packets_to_read: int) -> List[int]:
    result = []
    num_packets_read = 0
    while (
        len(bitstream) > 10
        and num_packets_to_read is None
        or (num_packets_to_read is not None and num_packets_read < num_packets_to_read)
    ):
        num_packets_read += 1
        version = read_bits(bitstream, 3)
        type_id = read_bits(bitstream, 3)
        if type_id == 4:  # literal
            literal = 0
            zero_found = False
            while not zero_found:
                literal <<= 4
                zero_found = read_bits(bitstream, 1) == 0
                literal += read_bits(bitstream, 4)
            # literal can be retrieved here
            result.append(literal)
        else:  # operator

            length_type_id = read_bits(bitstream, 1)
            if length_type_id == 0:
                total_length_subpackets = read_bits(bitstream, 15)
                subresult = part2_solution(deque([bitstream.popleft() for _ in range(total_length_subpackets)]), None)
            else:
                num_subpackets = read_bits(bitstream, 11)
                subresult = part2_solution(bitstream, num_subpackets)
            if type_id == 0:
                result.append(sum(subresult))
            elif type_id == 1:
                result.append(reduce(lambda x, acc: x * acc, subresult, 1))
            elif type_id == 2:
                result.append(min(subresult))
            elif type_id == 3:
                result.append(max(subresult))
            elif type_id == 5:
                if len(subresult) != 2:
                    raise AssertionError(subresult.__repr__())
                result.append(1 if subresult[0] > subresult[1] else 0)
            elif type_id == 6:
                if len(subresult) != 2:
                    raise AssertionError(subresult.__repr__())
                result.append(1 if subresult[0] < subresult[1] else 0)
            elif type_id == 7:
                if len(subresult) != 2:
                    raise AssertionError(subresult.__repr__())
                result.append(1 if subresult[0] == subresult[1] else 0)
    return result


def read_bits(bitstream: Deque[int], num_bits) -> int:
    """
    Returns the equivalent of the next n bits, where n is num_bits; removes from the front of the deque
    """
    result = 0
    for _ in range(num_bits):
        result <<= 1
        result += bitstream.popleft()
    return result


load_txt("input.txt")
print(part1_solution(deque(binary_str), None))
print(part2_solution(deque(binary_str), None))
