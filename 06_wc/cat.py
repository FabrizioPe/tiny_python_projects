#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-08
Purpose: Emulate the cat program
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate the cat program',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='File(s) to print',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='*',
                        default=[sys.stdin])

    parser.add_argument('-n',
                        '--number',
                        help='Print number of output lines',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise!"""

    args = get_args()
    start = 0
    for fh in args.file:
        for line_num, line in enumerate(fh, start=start+1):
            if args.number:
                print(f'{line_num:6}  ' + line, end='')
            else:
                print(line, end='')
            start = line_num


# --------------------------------------------------
if __name__ == '__main__':
    main()
