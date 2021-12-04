import pathlib
import importlib
import argparse
import logging
import sys

logger = logging.getLogger('AOC2021')
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

header = '-------------------------------'
entry = '  [-]'

INPUT_DIR = pathlib.Path(pathlib.Path(__file__).parent / 'inputs')

def main(args):
    logger.debug(header)
    day = args.day
    part = args.part
    sample = args.sample
    input_file = 'sample' if sample == True else 'input'

    input_filename = f'day{day}/{input_file}.txt'
    input_path = INPUT_DIR / input_filename
    with open(input_path, 'r') as f:
        inputs = [line.strip('\n') for line in f.readlines()]

    runner = importlib.import_module(f'src.day{day}')
    if part == '1':
        result = runner.part1(inputs)
    elif part == '2':
        result = runner.part2(inputs)
    logger.info(f'{entry} Results: {result}')
    logger.info(header)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run module with given input.')
    parser.add_argument('-D', '--day', dest='day', type=str, required=True, help="Which day's challenge to run.")
    parser.add_argument('-P', '--part', dest='part', type=str, required=True, help="Which part of the challenge to run.")
    parser.add_argument('--sample', dest='sample', action='store_true', help="Whether to use sample input.")
    args = parser.parse_args()
    main(args)