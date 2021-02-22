#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-22
Purpose: Scramble the middle letters of words
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble the letters of words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.str):
        args.str = open(args.str).read()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.str
    lines = text.splitlines()  # list of lines (recall that \n is lost!)

    splitter = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")  # compiled once, used a lot
    for line in lines:
        words = splitter.split(line)
        # print(''.join(map(scramble, words)))  # using map
        print(''.join(([scramble(word) for word in words])))  # using list comprehension


# --------------------------------------------------
def scramble(word):
    """Sort the middle letters of word into alphabetical order"""

    # words which must remain unchanged
    if len(word) <= 3 or re.match(r'\W+', word):
        return word

    middle_part = sorted(list(word[1:-1]))  # extract middle part and sort it alphabetically
    return word[0] + ''.join(middle_part) + word[-1]


# --------------------------------------------------
def test_scramble():
    assert scramble('the') == 'the'
    assert scramble('an') == 'an'
    assert scramble('banana') == 'baanna'
    assert scramble('mountain') == 'mainotun'
    assert scramble('Telephone') == 'Teehlnope'


# --------------------------------------------------
if __name__ == '__main__':
    main()
