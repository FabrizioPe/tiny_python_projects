#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-08
Purpose: Emulate the already installed word-count program
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # validate the input and returning a list of open file handles!
    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    tot_lines, tot_words, tot_bytes = 0, 0, 0
    for fh in args.file:
        num_lines, num_words, num_bytes = 0, 0, 0
        for line in fh:
            num_lines += 1
            num_bytes += len(line)
            num_words += len(line.split())
        tot_lines += num_lines
        tot_words += num_words
        tot_bytes += num_bytes
        print(f'{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}')

    if len(args.file) > 1:  # printing total if multiple files given
        print(f'{tot_lines:8}{tot_words:8}{tot_bytes:8} total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
