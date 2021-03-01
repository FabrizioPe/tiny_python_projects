#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-27
Purpose: Parsing csv files and creating text table output
         Input files checking included
"""

import argparse
import csv
import tabulate
from inputCheck import *


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
    fh = args.file

    # check for all kinds of bad file inputs
    check_empty(fh)
    check_headers_only(fh)
    # actually this func. is a bit too strict considering the program logic
    check_bad_headers(fh)
    check_bad_delimiters(fh)

    # if the file passes all the test, we can start the program:
    fh.seek(0)  # rewind the file
    random.seed(args.seed)
    csv_reader = csv.reader(args.file)  # create csv_reader object

    # extract all the records with well-formatted second column ('30-55')
    exercises = well_formatted_reps([row for i, row in enumerate(csv_reader)
                                     if i != 0])
    
    if not exercises:
        sys.exit(f'No usable data in {fh.name}')
    
    # randomly select args.num exercises, if possible
    if len(exercises) >= args.num:
        random_exc = random.sample(exercises, args.num)
    else:
        sys.exit(f'You cannot extract {args.num} exercises from a '
                 f'file with {len(exercises)} valid records.')

    # create workout of the day
    wod = []
    for exc, reps_int in random_exc:
        reps = random_reps(reps_int) // 2 if args.easy else random_reps(reps_int)
        wod.append((exc, reps))
    # the formatting of output is entirely handled by tabulate!!!
    print(tabulate.tabulate(wod, headers=('Exercise', 'Reps')))

    args.file.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
