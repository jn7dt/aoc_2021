import logging
from collections import namedtuple, Counter

from numpy import vectorize
logger = logging.getLogger('AOC2021')

coord = namedtuple('coord', ('x', 'y'))


class Line:
    def __init__(self, pair_one, pair_two):
        self.x1 = int(pair_one.split(',')[0])
        self.y1 = int(pair_one.split(',')[1])
        self.x2 = int(pair_two.split(',')[0])
        self.y2 = int(pair_two.split(',')[1])
    
    @property
    def horizontal(self):
        return self.y1 == self.y2
    
    @property
    def vertical(self):
        return self.x1 == self.x2
    
    @property
    def include(self):
        return self.horizontal or self.vertical
    
    @property
    def line_points(self):
        if self.include:
            for x in range(min(self.x1, self.x2), max(self.x1, self.x2)+1):
                for y in range(min(self.y1, self.y2), max(self.y1, self.y2)+1):
                    yield (x, y)
        else:
            x_distance = int(self.x2 - self.x1)
            x_dir = 1 if x_distance > 0 else -1
            y_distance = int(self.y2 - self.y1)
            y_dir = 1 if y_distance > 0 else -1
            for x, y in zip(
                range(0, x_distance + x_dir, x_dir),
                range(0, y_distance + y_dir, y_dir)
            ):
                yield (self.x1 + x, self.y1 + y)
                    


def part1(inputs):
    input_lines = []
    for line in inputs:
        pair_one, pair_two = line.split(' -> ')
        input_lines.append(Line(pair_one, pair_two))

    all_points = [coord for line in input_lines 
        for coord in line.line_points if line.include]
    
    point_counter = Counter(all_points) 
    return len([point for point, count in point_counter.items() if count >= 2])


def part2(inputs):
    input_lines = []
    for line in inputs:
        pair_one, pair_two = line.split(' -> ')
        input_lines.append(Line(pair_one, pair_two))

    all_points = [coord for line in input_lines 
        for coord in line.line_points]
    
    point_counter = Counter(all_points) 
    return len([point for point, count in point_counter.items() if count >= 2])