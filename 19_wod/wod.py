#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-26
Purpose: Parsing csv files and creating text table output
"""

import argparse
import csv
import random
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Workout Of (The) Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='CSV input file of exercises',
                        metavar='str',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='int',
                        type=int,
                        default=4)

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true')

    args = parser.parse_args()

    if args.num <= 0:
        parser.error(f'--num "{args.num}" must be greater than 0.')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    csv_reader = csv.reader(args.file)  # csv_reader object

    rows = [row for i, row in enumerate(csv_reader) if i != 0]
    random_rows = random.sample(rows, args.num)
    # calculate the width of left column in output
    lengths = [len(exercise) for exercise, _ in random_rows]
    lengths.append(10)
    width = max(lengths)

    # formatted output
    print('Exercise'.ljust(width) + '  ' + 'Reps'.rjust(6))
    print('-' * width + '  ' + '------')
    for exercise, interval in random_rows:
        reps = random_reps(interval) // 2 if args.easy else random_reps(interval)
        print(f'{exercise}'.ljust(width) + '  ' + f'{reps}'.rjust(6))


# --------------------------------------------------
def random_reps(interval: str) -> int:
    """Randomly determine reps from a given interval:
       Ex: '30-50' -> 42 """

    matches = re.search('([0-9]+)-([0-9]+)', interval)
    return random.randint(int(matches.group(1)), int(matches.group(2)))


# --------------------------------------------------
def test_random_reps():
    """Test random_reps"""
    state = random.getstate()
    random.seed(1)
    assert random_reps('10-30') == 14
    assert random_reps('50-90') == 86
    assert random_reps('25-50') == 50
    random.setstate(state)


# --------------------------------------------------
if __name__ == '__main__':
    main()
