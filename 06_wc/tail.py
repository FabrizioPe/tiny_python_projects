#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-09
Purpose: Emulate the tail program
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments."""

    parser = argparse.ArgumentParser(
        description='Emulate the tail program: print the last 10 (default) \
                    lines of files. If more than one file included, \
                    print headers.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        type=argparse.FileType('rt'),
                        nargs='*',
                        help='Input file(s)',
                        metavar='FILE',
                        default=[sys.stdin])

    parser.add_argument('-n',
                        '--lines',
                        type=str,
                        metavar='[+]NUM',
                        help='No. of last lines to output. If + included, start \
                             from NUM',
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
    """Make a jazz noise here."""

    args = get_args()
    lines_to_out = args.lines

    for fh in args.file:
        if args.verbose or len(args.file) > 1:
            print(f'===> {fh.name} <===')
        start = int(lines_to_out) - 1 if lines_to_out.startswith('+') \
            else file_len(fh.name) - int(lines_to_out)
        for i, line in enumerate(fh, start=1):
            if i > start:
                print(line, end='')
        print()
        fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
