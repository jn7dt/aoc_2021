import logging

logger = logging.getLogger('AOC2021')

def part1(inputs):
    '''count the number of times a depth measurement 
    increases from the previous measurement'''
    # logger.debug(len(inputs))
    int_inputs = [int(i) for i in inputs]
    return sum([1 for idx, i in enumerate(int_inputs[1:], start=1) if i > int_inputs[idx-1]])

def part2(inputs):
    '''count the number of times the sum of measurements in this 
    sliding window increases from the previous sum'''
    int_inputs = [int(i) for i in inputs]
    window_size = 3
    windows = [int_inputs[start:start+window_size] for start in range(0,len(int_inputs)-(window_size-1))]
    return sum([1 for idx, i in enumerate(windows[1:], start=1) if sum(i) > sum(windows[idx-1])])