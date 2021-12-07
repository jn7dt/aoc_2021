import logging
logger = logging.getLogger('AOC2021')

def simulate_fish(fish_state):
    new_state = dict()
    for i in range(1,9):
        new_state[i-1] = fish_state[i]

    new_state[6] += fish_state[0]
    new_state[8] = fish_state[0]

    return new_state 
            

def part1(inputs):
    '''
    full_timer: 6
    start_timer: 8
    end_value: 0
    '''
    fish_input = [int(j) for i in inputs for j in i.split(',')]
    fish_state = {
        i: 0 for i in range(9)
    }
    for fish in fish_input:
        fish_state[fish] += 1

    days = 80
    for day in range(days):
        fish_state = simulate_fish(fish_state)
    return sum([v for k,v in fish_state.items()])


def part2(inputs):
    fish_input = [int(j) for i in inputs for j in i.split(',')]
    fish_state = {
        i: 0 for i in range(9)
    }
    for fish in fish_input:
        fish_state[fish] += 1

    days = 256
    for day in range(days):
        fish_state = simulate_fish(fish_state)
    return sum([v for k,v in fish_state.items()])