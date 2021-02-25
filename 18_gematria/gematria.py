#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-25
Purpose: Find the most frequently occurring value and the corresponding words
"""

import argparse
import os
import re
from collections import Counter


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria with statistics',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.str):
        args.str = open(args.str).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    words = args.str.split()

    # build a list of tuples: [('234', 'hello'), ('97', 'a'), ('195', 'Zi')]
    num_word = [(word2num(word), re.sub('[^a-zA-Z0-9]', '', word)) for word in words]
    # statistics
    num_most_freq = Counter([num for num, _ in num_word]).most_common(1)[0][0]

    print(f'The most frequently occurring value is {num_most_freq}.')
    print('It corresponds to words:')
    for num, word in num_word:
        print(word) if num == num_most_freq else print(end='')


# --------------------------------------------------
def word2num(word: str) -> str:
    """Encode a word after removing non-word characters.
    Ex: "Don't" -> "Dont" -> '405'."""

    # remove non-alphabetic chars from the given word
    cleaned_word = re.sub('[^a-zA-Z0-9]', '', word)

    return str(sum(map(ord, cleaned_word)))


# --------------------------------------------------
def test_word2num():
    """Test word2num function"""
    assert word2num("a") == "97"
    assert word2num("abc") == "294"
    assert word2num("ab'c") == "294"
    assert word2num("4a-b'c") == "346"


# --------------------------------------------------
if __name__ == '__main__':
    main()
