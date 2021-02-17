#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-17
Purpose: Make rhyming words from a given word using regexes
"""

import argparse
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='A word to rhyme')

    args = parser.parse_args()

    if ' ' in args.str:
        parser.error('Please input a single word')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.str
    prefixes = [c for c in string.ascii_lowercase if c not in 'aeiou'] + \
        ('bl br ch cl cr dr fl fr gl gr pl pr sc '
        'sh sk sl sm sn sp st sw th tr tw thw wh wr '
        'sch scr shr sph spl spr squ str thr').split()

    splitted = stemmer(word)
    if not splitted[1]:
        print(f'Cannot rhyme "{word}"')
    else:
        rhymes = '\n'.join(sorted([prefix + splitted[1] for prefix in prefixes
                                   if prefix != splitted[0]]))

        print(rhymes)


# --------------------------------------------------
def stemmer(word):
    """Example: 'CHAIR' -> ('ch', 'air')
                'apple -> ('a', 'pple')"""

    consonants = ''.join((filter(lambda c: c not in 'aeiou', string.ascii_lowercase)))
    # consonants = ''.join([c for c in string.ascii_lowercase if c not in 'aeiou'])

    regex = f'([{consonants}]+)?([aeiou])(.+)'
    match = re.match(regex, word.lower())

    if match:
        p1 = match.group(1) or ''
        p2 = match.group(2)
        p3 = match.group(3)
        return p1, p2 + p3
    else:
        return word.lower(), ''  # bad input: signaled by second empty string


# --------------------------------------------------
def test_stemmer():
    # good input
    assert stemmer('CHAIR') == ('ch', 'air')
    assert stemmer('apple') == ('', 'apple')
    # bad input: signaled by second empty string
    assert stemmer('rxclfm') == ('rxclfm', '')
    assert stemmer('123') == ('123', '')


# --------------------------------------------------
if __name__ == '__main__':
    main()
