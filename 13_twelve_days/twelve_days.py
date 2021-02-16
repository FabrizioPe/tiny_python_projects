#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-16
Purpose: Reproducing the "12 days of Christmas" song
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments."""

    parser = argparse.ArgumentParser(
        description='Twelve Days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='days',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()

    if not 1 <= args.num <= 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here."""

    args = get_args()

    # 1)
    # for day in range(1, args.num + 1):
    #     print(verse(day), file=args.outfile)
    #     if day != args.num:
    #         print(file=args.outfile)

    # 2)
    print('\n\n'.join(map(verse, range(1, args.num + 1))), file=args.outfile)


# --------------------------------------------------
def verse(day):
    """Return the day-th verse of the song."""

    ordinal = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth',
               6: 'sixth', 7: 'seventh', 8: 'eighth', 9: 'ninth', 10: 'tenth',
               11: 'eleventh', 12: 'twelfth'}

    with open('../inputs/gifts.txt') as fh:
        gifts = [line.strip() for line in fh.readlines()]
        gifts.insert(0, 'placeholder')
        gifts[1] = 'And a partridge in a pear tree.' if day != 1 else gifts[1]

    return f'On the {ordinal[day]} day of Christmas,\n' + \
            'My true love gave to me,\n' +\
           '\n'.join([gifts[gift] for gift in range(day, 0, -1)])


# --------------------------------------------------
def test_verse():

    assert verse(1) == '\n'.join(['On the first day of Christmas,',
                                 'My true love gave to me,',
                                 'A partridge in a pear tree.'])

    assert verse(2) == '\n'.join(['On the second day of Christmas,',
                                  'My true love gave to me,',
                                  'Two turtle doves,',
                                  'And a partridge in a pear tree.'])


# --------------------------------------------------
if __name__ == '__main__':
    main()
