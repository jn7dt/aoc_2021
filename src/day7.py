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
    jitter = 1
    logger.debug(f'mean: {mean_pos}')
    total_fuel = sum([sum([j for j in range(1, abs(i - mean_pos)+1)]) for i in positions])
    low_pos = mean_pos - jitter
    high_pos = mean_pos + jitter
    low_fuel = sum([sum([j for j in range(1, abs(i - low_pos)+1)]) for i in positions])
    high_fuel = sum([sum([j for j in range(1, abs(i - high_pos)+1)]) for i in positions])
    logger.debug(f'Mean Fuel: {total_fuel:,}')
    logger.debug(f'Low Fuel: {low_fuel:,}')
    logger.debug(f'High Fuel: {high_fuel:,}')
    # return total_fuel