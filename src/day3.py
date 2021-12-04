from collections import Counter
from bitstring import BitArray
import logging
logger = logging.getLogger('AOC2021')

def transpose_input(inputs):
    input_length = len(inputs[0])
    return [[int(input_arr[i]) for input_arr in inputs]
     for i in range(input_length)]


def part1(inputs):
    '''Use the binary numbers in your diagnostic report to 
    calculate the gamma rate and epsilon rate, then multiply 
    them together. What is the power consumption of the 
    submarine? (Be sure to represent your answer in decimal, 
    not binary.)'''

    transpose = transpose_input(inputs)
    gamma = ''.join(['1' if sum(t) > (len(t) / 2) else '0' for t in transpose])
    g = BitArray(bin=gamma)
    gamma = g.bin
    logger.debug(f'  [+] Gamma: {gamma}')
    e = BitArray(bin=gamma)
    e.invert()
    epsilon = e.bin
    logger.debug(f'  [+] Epsilon: {epsilon}')
    return g.uint * e.uint

def find_most_common(numbers, use_one=True):
    count = sum(numbers)
    half = len(numbers) / 2
    if count > half:
        return '1' if use_one is True else '0'
    elif count < half:
        return '0' if use_one is True else '1'
    elif count == half:
        return f'{int(use_one)}'

def find_rating(inputs, oxygen=True):
    input_length = len(inputs[0])
    filtered_inputs = inputs[:]
    for bit in range(input_length):
        bits = [int(i[bit]) for i in filtered_inputs]
        most_common = find_most_common(bits, use_one=oxygen)
        filtered_inputs = [i for i in filtered_inputs if i[bit] == most_common]
        if len(filtered_inputs) == 1:
            return filtered_inputs
    return []

def part2(inputs):
    oxygen_rating = ''.join(find_rating(inputs, oxygen=True))
    logger.debug(f'  [+] O2 Rating: {oxygen_rating}')
    co2_rating = ''.join(find_rating(inputs, oxygen=False))
    logger.debug(f'  [+] CO2 Rating: {co2_rating}')
    
    o = BitArray(bin=oxygen_rating)
    c = BitArray(bin=co2_rating)
    return o.uint * c.uint
