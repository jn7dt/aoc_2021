import logging
logger = logging.getLogger('AOC2021')

def adjust_position(current_position, command):
    direction, amount = command.split()
    amount = int(amount)
    match direction:
        case "forward":
            current_position[0] += amount
        case "down":
            current_position[1] += amount
        case "up":
            current_position[1] -= amount
    return current_position


def part1(inputs):
    '''Calculate the horizontal position and depth you would 
    have after following the planned course. What do you get 
    if you multiply your final horizontal position by your final depth?'''
    position = [0, 0]
    for i in inputs:
        position = adjust_position(position, i)
    return position[0] * position[1]

def adjust_aim(current_aim, command):
    direction, amount = command.split()
    amount = int(amount)
    match direction:
        case "forward":
            current_aim[0] += amount
            current_aim[1] += (current_aim[2] * amount) 
        case "down":
            current_aim[2] += amount
        case "up":
            current_aim[2] -= amount
    return current_aim

def part2(inputs):
    '''calculate the horizontal position and depth you would 
    have after following the planned course. What do you get 
    if you multiply your final horizontal position by your 
    final depth?'''
    aim = [0, 0, 0]
    for i in inputs:
        aim = adjust_aim(aim, i)
    return aim[0] * aim[1]