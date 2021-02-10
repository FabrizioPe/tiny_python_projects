#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-10
Purpose: Gashlycrumb: interactive version
"""

import argparse
# from pprint import pprint as pp


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb: interactive version',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

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

    # searching the dictionary interactively
    while True:
        letter = (input('Please provide a letter [! to quit]: ')).lower()
        if letter == '!':
            print('Bye')
            break
        else:
            print(lett_sent.get(letter, f'I do not know "{letter}".'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
