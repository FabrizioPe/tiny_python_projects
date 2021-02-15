#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-15
Purpose: Reproduce "99 bottles of beer" song: 'going further' section
Note: tests have been updated only partially
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song ("going further" version)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles initially on the wall',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-s',
                        '--step',
                        help='How many bottles at each verse',
                        metavar='int',
                        type=int,
                        default=1)

    parser.add_argument('-r',
                        '--reverse',
                        help='Count up instead of down',
                        action='store_true', )

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    if not args.reverse and args.num > 10:
        parser.error('No more than 10 beers when going down, please!')

    if args.reverse and args.num > 9:
        parser.error('No more than 9 beers when going up, please!')

    if args.step < 1:
        parser.error(f'--step "{args.step}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    step = args.step

    # 1) for loop
    # for i in range(args.num, 0, -1):
    #     print(verse(i))
    #     if i != 1:
    #         print()

    # 2) list comprehension
    if args.reverse:
        print('\n\n'.join([verse(i, step, args.reverse) for i in range(args.num, 10, step)]))
    else:
        print('\n\n'.join([verse(i, step) for i in range(args.num, 0, -step)]))

    # 3) map function
    # print('\n\n'.join(map(verse, (range(args.num, 0, step)))))


# --------------------------------------------------
def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join(['One bottle of beer on the wall,',
                                    'One bottle of beer,',
                                    'Take one down, pass it around,',
                                    'No more bottles of beer on the wall!'])

    two_bottles = verse(2)
    assert two_bottles == '\n'.join(['Two bottles of beer on the wall,',
                                     'Two bottles of beer,',
                                     'Take one down, pass it around,',
                                     'One bottle of beer on the wall!'])

    step_two = verse(3, step=2)
    assert step_two == '\n'.join(['Three bottles of beer on the wall,',
                                  'Three bottles of beer,',
                                  'Take two down, pass it around,',
                                  'One bottle of beer on the wall!'])

    reverse = verse(3, step=1, reverse=True)
    assert reverse == '\n'.join(['Three bottles of beer on the wall,',
                                 'Three bottles of beer,',
                                 'Put one up,',
                                 'Four bottles of beer on the wall!'])

    reverse_step = verse(3, step=2, reverse=True)
    assert reverse_step == '\n'.join(['Three bottles of beer on the wall,',
                                      'Three bottles of beer,',
                                      'Put two up,',
                                      'Five bottles of beer on the wall!'])


# --------------------------------------------------
def verse(num_bottles, step=1, reverse=False):
    """Return one verse of the song."""

    text_num = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
                7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten'}

    if reverse:
        left_bottles = text_num.get(num_bottles + step, 'Ten or more')
        num_bottles = text_num[num_bottles]

        return '\n'.join([f'{num_bottles} bottles of beer on the wall,',
                          f'{num_bottles} bottles of beer,',
                          f'Put {text_num.get(step, "Lots of them").lower()} up,',
                          f'{left_bottles} bottles of beer on the wall!'])
    else:
        if num_bottles - step > 0:
            bottles, left_bottles = 'bottles', text_num[num_bottles - step]
            bottles_minus = 'bottles' if num_bottles - step > 1 else 'bottle'
            num_bottles = text_num[num_bottles]
        else:
            left_bottles, bottles_minus = 'No more', 'bottles'
            if num_bottles == 1:
                num_bottles, bottles = 'One', 'bottle'
            else:
                num_bottles, bottles = text_num[num_bottles], 'bottles'

        return '\n'.join([f'{num_bottles} {bottles} of beer on the wall,',
                          f'{num_bottles} {bottles} of beer,',
                          f'Take {text_num[step].lower()} down, pass it around,',
                          f'{left_bottles} {bottles_minus} of beer on the wall!'])


# --------------------------------------------------
if __name__ == '__main__':
    main()
