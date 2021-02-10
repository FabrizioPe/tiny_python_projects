#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-10
Purpose: Build a phonebook from a given file
"""

import argparse
from pprint import pprint


# --------------------------------------------------
def get_args():
    """Get command-line arguments."""

    parser = argparse.ArgumentParser(
        description='Phonebook from a file containing names, tel. nums and emails',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Space-separated file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here."""

    args = get_args()
    fh = args.file

    phonebook = dict()
    for i, line in enumerate(fh, start=1):
        # splitting data with ' ' (the required file format)
        data = line.split()
        if len(data) <= 1:
            print(f'Look at line {i} in {fh.name}: apparently data are missing')
            continue
        if len(data[1:]) == 1:
            phonebook[data[0].title()] = data[1]
        else:
            phonebook[data[0].title()] = (data[1], data[2])

    print()
    pprint(phonebook)


# --------------------------------------------------
if __name__ == '__main__':
    main()
