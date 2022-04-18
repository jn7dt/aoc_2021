import logging
from statistics import mean, median, mode


logger = logging.getLogger('AOC2021')

def part1(inputs):
    positions = [int(i) for i in inputs[0].split(',')]
    median_pos = int(median(positions))
    return sum([abs(i - median_pos) for i in positions])

def part2(inputs):
    positions = [int(i) for i in inputs[0].split(',')]
    mean_pos = int(mean(positions))
    return sum([sum([j for j in range(1, abs(i - mean_pos)+1)]) for i in positions])