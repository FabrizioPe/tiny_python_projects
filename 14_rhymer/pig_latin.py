#!/usr/bin/env python3
"""
Author: FabrizioPe
Date: 2021-02-18
Purpose: Pig Latin
"""

import argparse
import os

from rhymer import stemmer


# -------------------------------------
def get_args():
    """Get command-line arguments."""

    parser = argparse.ArgumentParser(
        description='Pig Latin',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Input word')

    args = parser.parse_args()

    if ' ' in args.str:
        parser.error('Please insert a single word')

    if os.path.isfile(args.str) or '.' in args.str:
        parser.error('Please insert a word, not a file')

    return args


# -------------------------------------
def pig_latin(stemmed_word: tuple):
    """Return the pig latin string of the given tuple.
       Ex: (a, pple) -> appleyay / (cat) -> atcay"""

    start, end = stemmed_word
    if start.startswith(('a', 'e', 'i', 'o', 'u')):
        return start + end + 'yay'
    else:
        return end + start + 'ay'


# -------------------------------------
def test_pig_latin():
    assert pig_latin(('c', 'at')) == 'atcay'
    assert pig_latin(('a', 'pple')) == 'appleyay'
    assert pig_latin(('ch', 'air')) == 'airchay'


# -------------------------------------
def main():

    args = get_args()
    word = args.str

    stemmed_word = stemmer(word)
    if stemmed_word[1] == '':
        print(f'Cannot translate {word} to pig latin.')
    else:
        print(pig_latin(stemmed_word))


# -------------------------------------
if __name__ == '__main__':
    main()
