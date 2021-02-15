#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-15
Purpose: Randomly uppercase letters in a text
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
    """Randomly uppercase letter"""
    return letter.upper() if random.choice([0, 1]) else letter.lower()


# --------------------------------------------------
def test_choose():
    state = random.getstate()
    random.seed(1)
    assert choose('a') == 'a'
    assert choose('b') == 'b'
    assert choose('c') == 'C'
    assert choose('d') == 'd'
    random.setstate(state)


# --------------------------------------------------
if __name__ == '__main__':
    main()
