#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-18
Purpose: Make rhyming words from given word(s) using regexes
         Extension 4 from 'going further': optionally using consonants 
         extracted from a 'dictionary' and only print words that are found
         in that dictionary (see ../inputs/words.txt for a valid dictionary)
"""

import argparse
import os
import re
import string
import sys
from subprocess import getoutput

from consonant_analysis import dictionary_consonants


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words". If you give more than one word,\
                    an output file for each word will be written.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        type=str,
                        help='Input string or file')

    parser.add_argument('-d',
                        '--dictionary',
                        metavar='dict',
                        type=argparse.FileType('rt'),
                        help='Input "dictionary" used for consonant extraction '
                             'and rhymes validation')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file [ignored if more than one word given]',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()

    # in both cases, get_args returns a list of words (from str to list...unorthodox?)
    if os.path.isfile(args.str):
        fh = open(args.str)
        words = [word for line in fh for word in line.split()]
        words = [word.rstrip(string.punctuation) for word in words]
        args.str = words
        fh.close()
    else:
        args.str = [word.rstrip(string.punctuation) for word in args.str.split()]

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fh = args.outfile
    dictionary_fh = args.dictionary
    words = args.str  # read the list of words from a file or (just one) from stdin
    if len(words) > 1:
        getoutput(f'rm {out_fh.name}')

    if dictionary_fh:  # read the given dictionary and extract consonant sounds
        dictionary = set(dictionary_fh.read().split('\n'))
        prefixes = list(dictionary_consonants(dictionary))
    else:
        prefixes = [c for c in string.ascii_lowercase if c not in 'aeiou'] + \
        ('bl br ch cl cr dr fl fr gl gr pl pr sc '
        'sh sk sl sm sn sp st sw th tr tw thw wh wr '
        'sch scr shr sph spl spr squ str thr').split()

    # produce the rhyming words
    for word in words:
        if len(words) > 1:
            out_fh = open(f'./files/{word}.txt', 'wt')
        splitted = stemmer(word)
        if not splitted[1]:
            print(f'Cannot rhyme "{word}"', file=out_fh)
        else:
            if dictionary_fh:  # also check if the rhyme is in the dictionary!
                rhymes = '\n'.join(sorted([prefix + splitted[1] for prefix in prefixes
                                           if prefix != splitted[0] and (prefix + splitted[1]) in dictionary]))
            else:
                rhymes = '\n'.join(sorted([prefix + splitted[1] for prefix in prefixes
                                       if prefix != splitted[0]]))
            print(rhymes, file=out_fh)
        out_fh.close()


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
