from fnmatch import translate
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

def arrange_signal(signal):
    return ''.join(sorted(signal))

def compare_signals(signal_a, signal_b):
    return [s for s in signal_a if s not in signal_b]

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
    numbers = {
        k: {
            'segments': v,
            'length': len(v)
        }
        for k, v in numbers.items()
    }
    lengths_numbers = dict()
    for k, v in numbers.items():
        lengths_numbers.setdefault(v['length'], []).append(k)
    segment_lengths = dict()
    switched_numbers = {k: '' for k, v in numbers.items()}
    
    signal_patterns = [arrange_signal(signal) for signal in signal_patterns]

    for signal_pattern in signal_patterns:
        segment_lengths.setdefault(len(signal_pattern), []).append(signal_pattern)
        match len(signal_pattern):
            case 2:
                switched_numbers[1] = signal_pattern
            case 3:
                switched_numbers[7] = signal_pattern
            case 4:
                switched_numbers[4] = signal_pattern
            case 7:
                switched_numbers[8] = signal_pattern
    
    segments['a'] = compare_signals(switched_numbers[7], switched_numbers[1])[0]
    
    for signal_pattern in segment_lengths[6]:
        comp = compare_signals(signal_pattern, switched_numbers[4] + segments['a'])
        if len(comp) == 1:
            switched_numbers[9] = signal_pattern
            segments['g'] = comp[0]
    
    segments['e'] = compare_signals(switched_numbers[8], switched_numbers[9])[0]
    
    '''
    Numbers found: 1, 4, 7, 8, 9 (Need: 0, 2, 3, 5, 6)
    Segments found: a, e, g (Need b, c, d, f)
    '''
    for signal_pattern in segment_lengths[6]:
        if signal_pattern != switched_numbers[9]:
            comp = compare_signals(switched_numbers[1], signal_pattern)
            if len(comp) == 0:
                switched_numbers[0] = signal_pattern
                four_set = switched_numbers[4]
                combo_set = compare_signals(signal_pattern, [segments['a'], segments['e'], segments['g']])
                segments['d'] = compare_signals(four_set, combo_set)[0]
            elif len(comp) == 1:
                switched_numbers[6] = signal_pattern
                segments['c'] = comp[0]
    
    segments['b'] = compare_signals(switched_numbers[4], switched_numbers[1] + segments['d'])[0]

    segments['f'] = [c for c in switched_numbers[1] if c != segments['c']][0] 

    # signal_mapping = '\n'.join([
    #     f' {segments["a"]*4} ',
    #     f'{segments["b"]}    {segments["c"]}',
    #     f'{segments["b"]}    {segments["c"]}',
    #     f' {segments["d"]*4} ',
    #     f'{segments["e"]}    {segments["f"]}',
    #     f'{segments["e"]}    {segments["f"]}',
    #     f' {segments["g"]*4} '
    # ])
    # logger.debug(signal_mapping)

    return {v: k for k, v in segments.items()}

def decode_outputs(outputs, segment_map):
    return [
        ''.join(sorted([segment_map[c] for c in output]))
        for output in outputs
    ]

def translate_outputs(outputs):
    numbers = {v: str(k) for k, v in {
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
        }.items()
    }
    return int(''.join([
        numbers[output] for output in outputs
    ]))
    
def part2(inputs):
    total_outputs = 0
    for entry in inputs:
        signal_patterns, output_values = entry.split(' | ')
        signal_patterns = signal_patterns.split()
        segment_map = decode_signals(signal_patterns)
        output_values = output_values.split()
        decoded_outputs = decode_outputs(output_values, segment_map)
        output_numbers = translate_outputs(decoded_outputs)
        total_outputs += output_numbers
    return total_outputs

