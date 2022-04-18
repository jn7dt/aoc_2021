import logging
logger = logging.getLogger('AOC2021')

def part1(inputs):
    unique_segments = [2, 3, 4, 7]
    target_digits = 0
    for entry in inputs:
        signal_patterns, output_values = entry.split(' | ')
        for output_value in output_values.split():
            if len(output_value) in unique_segments:
                target_digits += 1
    return target_digits

def decode_signals(signal_patterns):
    segments = {
        'a': None,
        'b': None,
        'c': None,
        'd': None,
        'e': None,
        'f': None,
        'g': None
    }
    numbers = {
        0: 'abcefg',
        1: 'cf',
        2: 'acdeg',
        3: 'acdfg',
        4: 'bcdf',
        5: 'abdfg',
        6: 'abdefg',
        7: 'acf',
        8: 'abcdefg',
        9: 'abcdfg'
    }
    switched_numbers = numbers.copy()

    for signal_pattern in signal_patterns:
        match len(signal_pattern):
            case 2:
                switched_numbers[1] = signal_pattern
            case 3:
                switched_numbers[7] = signal_pattern
            case 4:
                switched_numbers[4] = signal_pattern
            case 7:
                switched_numbers[8] = signal_pattern
    
    for c in switched_numbers[7]:
        if c not in switched_numbers[1]:
            segments['a'] = c
    
    switched_numbers[9] = switched_numbers[4] + segments['a']

    for signal_pattern in signal_patterns:
        if len(signal_pattern) == 6:
            signal_chars = set(signal_pattern)
            nine_chars = switched_numbers[9]
            if len(signal_chars - nine_chars) == 1:
                g = list(signal_chars - nine_chars)
                segments['g'] = g[0]
    
    set_e = list(set(switched_numbers[8]) - set(switched_numbers[9]))[0]
    segments['e'] = set_e


    '''
    Decoding steps:
        1 + 7 = a
        4 + a + 9 = g
        9 + 8 = e
        0 (aeg) - 4 (bcf) = d -- won't work without knowing which signal is 0
        2 - adeg = c
        1 - c = f
        4 - cdf = b
    '''

    pass

def part2(inputs):
    for entry in inputs:
        signal_patterns, output_values = entry.split(' | ')
        signal_patterns = signal_patterns.split()
        decode_signals(signal_patterns)
        output_values = output_values.split()