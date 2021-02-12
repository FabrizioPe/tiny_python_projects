#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-11
Purpose: A random insults generator
"""

import argparse
import os
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Heap abuse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--adjectives',
                        help='Number of adjectives',
                        metavar='adjectives',
                        type=int,
                        default=2)

    parser.add_argument('-n',
                        '--number',
                        help='Number of insults',
                        metavar='insults',
                        type=int,
                        default=3)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-af',
                        '--adj_file',
                        metavar='adj_file',
                        type=argparse.FileType('rt'),
                        help='File containing adjectives',
                        default='../inputs/adjectives.txt')

    parser.add_argument('-nf',
                        '--noun_file',
                        metavar='noun_file',
                        type=argparse.FileType('rt'),
                        help='File containing nouns',
                        default='../inputs/nouns.txt')

    args = parser.parse_args()

    # handling negative/zero input (argparse is not doing that)
    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    if os.stat(args.adj_file.name).st_size == 0:
        parser.error(f'{os.path.basename(args.adj_file.name)} looks empty')

    if os.stat(args.noun_file.name).st_size == 0:
        parser.error(f'{os.path.basename(args.noun_file.name)} looks empty')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    adjs_list = args.adj_file.read().strip().split()
    nouns_list = args.noun_file.read().strip().split()

    for _ in range(args.number):
        insult = f"You {', '.join(random.sample(adjs_list, args.adjectives))} " \
                 f"{random.choice(nouns_list)}!"
        print(insult)


# --------------------------------------------------
if __name__ == '__main__':
    main()
