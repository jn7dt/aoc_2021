import logging
import numpy as np
from numpy import ma
from numpy.ma.core import nomask
logger = logging.getLogger('AOC2021')

def check_board(board_mask):
    columns = board_mask.sum(axis=0)
    rows = board_mask.sum(axis=1)
    if 5 in columns or 5 in rows:
        return True
    else:
        return False

def update_board(board_mask, draw):
    draw_mask = ma.masked_values(board_mask.data, draw)
    return board_mask.mask + draw_mask.mask

def part1(inputs):
    number_draws = [int(i) for i in inputs[0].split(',')]
    board_size = 5
    matrices = [
        np.array([[int(i) for i in j.split()] for j in matrix])
        for matrix in [inputs[start:start+board_size]
        for start in range(2, len(inputs[2:]), board_size+1)]
    ]
    first_draw = number_draws[0]
    masks = [ma.masked_values(board, first_draw) for board in matrices]
    for draw in number_draws[1:]:
        for mask in masks:
            mask.mask = update_board(mask, draw)
            if mask.mask is not nomask:
                winning = check_board(mask.mask)
                if winning == True:
                    return sum(mask.data[~mask.mask]) * draw
  

def part2(inputs):
    number_draws = [int(i) for i in inputs[0].split(',')]
    board_size = 5
    matrices = [
        np.array([[int(i) for i in j.split()] for j in matrix])
        for matrix in [inputs[start:start+board_size]
        for start in range(2, len(inputs[2:]), board_size+1)]
    ]
    first_draw = number_draws[0]
    masks = [ma.masked_values(board, first_draw) for board in matrices]
    winning_boards = []
    last_draw = 0
    for draw in number_draws[1:]:
        for idx, mask in enumerate(masks):
            if idx not in winning_boards:
                mask.mask = update_board(mask, draw)
                if mask.mask is not nomask:
                    winning = check_board(mask.mask)
                    if winning == True:
                        winning_boards.append(idx)
                        last_draw = draw
    last_board = masks[winning_boards[-1]]
    return sum(last_board.data[~last_board.mask]) * last_draw