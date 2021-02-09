#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-09
Purpose: Emulate the tac program
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments."""

    parser = argparse.ArgumentParser(
        description='Emulate the tac program: print file(s) last line first.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        type=argparse.FileType('rt'),
                        nargs='*',
                        help='Input file(s)',
                        metavar='FILE',
                        default=[sys.stdin])

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

    for fh in args.file:
        # note: this is not memory efficient, because the whole file is
        # read into memory as a list...
        for line in reversed(fh.readlines()):
            print(line, end='')
        fh.close()

# --------------------------------------------------
if __name__ == '__main__':
    main()