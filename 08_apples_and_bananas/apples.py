#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-10
Purpose: Find and replace vowels in a given text
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='str',
                        choices='aeiou',
                        type=str,
                        default='a')

    args = parser.parse_args()

    # but will this file remain open?
    if os.path.isfile(args.str):
        args.str = open(args.str).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.str
    vowel = args.vowel

    table = {'a': vowel, 'e': vowel, 'i': vowel, 'o': vowel, 'u': vowel,
             'A': vowel.upper(), 'E': vowel.upper(), 'I': vowel.upper(),
             'O': vowel.upper(), 'U': vowel.upper()}

    # apply the transformation defined in the table, to the input text
    print(text.translate(str.maketrans(table)))

# --------------------------------------------------
if __name__ == '__main__':
    main()
