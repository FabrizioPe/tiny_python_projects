#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-14
Purpose: Reproduce "99 bottles of beer" song
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='int',
                        type=int,
                        default=10)
    
    args = parser.parse_args()
    
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # 1) for loop
    # for i in range(args.num, 0, -1):
    #     print(verse(i))
    #     if i != 1:
    #         print()

    # 2) list comprehension
    # print('\n\n'.join([verse(i) for i in range(args.num, 0, -1)]))

    # 3) map function
    print('\n\n'.join(map(verse, range(args.num, 0, -1))))


# --------------------------------------------------
def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join(['1 bottle of beer on the wall,',
                                   '1 bottle of beer,',
                                   'Take one down, pass it around,',
                                   'No more bottles of beer on the wall!'])

    two_bottles = verse(2)
    assert two_bottles == '\n'.join(['2 bottles of beer on the wall,',
                                     '2 bottles of beer,',
                                     'Take one down, pass it around,',
                                     '1 bottle of beer on the wall!'])


# --------------------------------------------------
def verse(num_bottles):
    """Return one verse of the song."""

    if num_bottles >= 2:
        bottles, left_bottles = 'bottles', num_bottles - 1
        bottles_minus = 'bottles' if num_bottles > 2 else 'bottle'
    else:
        bottles, left_bottles, bottles_minus = 'bottle', 'No more', 'bottles'

    return '\n'.join([f'{num_bottles} {bottles} of beer on the wall,',
                      f'{num_bottles} {bottles} of beer,',
                      'Take one down, pass it around,',
                      f'{left_bottles} {bottles_minus} of beer on the wall!'])


# --------------------------------------------------
if __name__ == '__main__':
    main()
