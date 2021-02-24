#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-24
Purpose: Find all balanced/unbalanced pairs in a given text
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find balanced/unbalanced pairs of parentheses',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text1 = args.file.read().strip()

    roundp = re.findall(r'\(+\b.*?\b\)+', text1)
    balancedr = [group for group in roundp
                 if len(re.findall(r'\(', group)) == len(re.findall(r'\)', group))]
    unbalancedr = [group for group in roundp if group not in balancedr]

    squarep = re.findall(r'[\[]+\b.*?\b[]]+', text1)
    balanceds = [group for group in squarep
                 if len(re.findall(r'\[', group)) == len(re.findall(r']', group))]
    unbalanceds = [group for group in squarep if group not in balanceds]

    curlyp = re.findall(r'[{]+\b.*?\b[}]+', text1)
    balancedc = [group for group in curlyp
                 if len(re.findall(r'{', group)) == len(re.findall(r'}', group))]
    unbalancedc = [group for group in curlyp if group not in balancedc]

    if len(squarep + roundp + curlyp) == 0:
        sys.exit(f'"{args.file.name}" has no parentheses.')

    print(f'The balanced parentheses are: {balancedr + balanceds + balancedc}')
    print(f'The unbalanced parentheses are: {unbalancedr + unbalanceds + unbalancedc}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
