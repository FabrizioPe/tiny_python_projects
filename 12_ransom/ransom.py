#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-15
Purpose: Randomly encode letters in a text ('going further')
"""

import argparse
import os
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().strip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    random.seed(args.seed)

    # 1)
    # text_list = list(text)
    # print(''.join([choose(letter) for letter in text_list]))

    # 2)
    # this is an example of map/reduce processing (potentially can be parallelized)
    print(''.join(map(choose, text)))

    # 3)
    # ransom = ''
    # for char in text:
    #     ransom += choose(char)
    # print(ransom)


# --------------------------------------------------
def choose(letter):
    """Randomly encode letter"""

    enc = {'A': '4', 'B': '|3', 'C': '(', 'D': '|)', 'E': '3', 'F': '|=',
           'G': '(-', 'H': '|-|', 'I': '1', 'J': '_|', 'K': '|<', 'L': '|_',
           'M': '==', 'N': '|=|', 'P': '|`', 'S': '5', 'T': '+', 'V': '%',
           'W': '6'}

    return enc.get(letter.upper(), '$') if random.choice([0, 1]) else letter


# --------------------------------------------------
def test_choose():
    state = random.getstate()
    random.seed(1)
    assert choose('h') == 'h'
    assert choose('p') == 'p'
    assert choose('t') == '+'
    assert choose('w') == 'w'
    assert choose('b') == '|3'
    random.setstate(state)


# --------------------------------------------------
if __name__ == '__main__':
    main()
