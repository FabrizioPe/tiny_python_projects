#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-09
Purpose: Emulate the head program
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments."""

    parser = argparse.ArgumentParser(
        description='Emulate the head program. If more than one file is \
            included, print also the file name as header.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        type=argparse.FileType('rt'),
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='*',
                        default=[sys.stdin])

    parser.add_argument('-n',
                        '--lines',
                        metavar='[-]NUM',
                        type=int,
                        help='Num. of lines to print. If - is included, print\
                             all but the last N lines.',
                        default=10)

    parser.add_argument('-v',
                        '--verbose',
                        help='Include header of files.',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def file_len(filename):
    with open(filename) as fh:
        i = -1
        for i, l in enumerate(fh):
            pass
        return i + 1


# --------------------------------------------------
def main():
    """Make a jazz noise here!"""

    args = get_args()
    lines_to_print = args.lines

    for fh in args.file:
        if args.verbose or len(args.file) > 1:
            print(f'===> {fh.name} <===')
        if lines_to_print >= 0:
            for i in range(lines_to_print):
                print(fh.readline(), end='')
        else:
            for i in range(file_len(fh.name) + lines_to_print):
                print(fh.readline(), end='')
        print()
        fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
