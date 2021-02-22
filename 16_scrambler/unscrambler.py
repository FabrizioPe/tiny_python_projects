#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-22
Purpose: Unscramble a scrambled text: restore it back to original
"""

import argparse
from collections import Counter
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Unscramble a scrambled text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-d',
                        '--dictionary',
                        metavar='dictionary',
                        type=argparse.FileType('rt'),
                        help='Reference English dictionary',
                        default='../inputs/words.txt')

    args = parser.parse_args()

    if os.path.isfile(args.str):
        args.str = open(args.str).read()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    dict_path = args.dictionary.name
    
    text = args.str
    lines = text.splitlines()  # list of lines (recall that \n is lost!)

    splitter = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")  # compiled once, used a lot
    for line in lines:
        words = splitter.split(line)
        # print(''.join(map(scramble, words)))  # using map
        print(''.join(([unscramble(word, dict_path) for word in words])))  # using list comprehension


# --------------------------------------------------
def unscramble(word: str, dictionary: str):
    """Restore word: tltrue -> turtle"""

    # return little words or punctuation clusters unchanged
    if len(word) <= 3 or re.match(r'\W+', word):
        return word

    # build a set of candidates for the given scrambled word, using the given
    # English dictionary
    with open(dictionary) as dict_fh:
        words = set(dict_fh.read().strip().split('\n'))
        candidates = list()
        for w in words:
            if (w[0].lower(), w[-1], len(w)) == (word[0].lower(), word[-1], len(word)):
                candidates.append(w)

    # check if one of the candidates has the same composition of word
    for candidate in candidates:
        if Counter(word.lower()) == Counter(candidate.lower()):
            return candidate.lower() if word[0].islower() else candidate.title()

    return None


# --------------------------------------------------
def test_unscramble():
    assert unscramble('the', '../inputs/words.txt') == 'the'
    assert unscramble('an', '../inputs/words.txt') == 'an'
    assert unscramble('bnnaaa', '../inputs/words.txt') == 'banana'
    assert unscramble('miatnuon', '../inputs/words.txt') == 'mountain'
    assert unscramble('Thpolenee', '../inputs/words.txt') == 'Telephone'


# --------------------------------------------------
if __name__ == '__main__':
    main()
