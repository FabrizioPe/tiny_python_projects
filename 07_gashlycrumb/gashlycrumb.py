#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-09
Purpose: Gashlycrumb, look items up in a dictionary
"""

import argparse
from pprint import pprint as pp


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        nargs='+',
                        help='Letter(s)')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # building the dictionary
    lett_sent = {}
    for line in args.file:
        lett_sent[line[0].lower()] = line.rstrip()

    # print a pretty version of the dictionary. Leave it here for ref.
    # pp(lett_sent)

    # searching the dictionary
    for letter in args.letter:
        print(lett_sent.get(letter.lower(), f'I do not know "{letter}".').rstrip())


# --------------------------------------------------
if __name__ == '__main__':
    main()
