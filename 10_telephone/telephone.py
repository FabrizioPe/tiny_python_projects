#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-12
Purpose: Reproducing the "telephone" game
"""

import argparse
import os
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        args.text = open(args.text).read().strip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    orig_text = args.text
    mutations = args.mutations
    random.seed(args.seed)

    # determining the characters to change
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))
    num_mutations = round(mutations * len(orig_text))
    indexes = random.sample(range(len(orig_text)), num_mutations)

    # random mutation phase
    mutated_text = orig_text  # the mutated text is at first the original text
    for i in indexes:
        alpha_reduced = alpha.replace(orig_text[i], '')
        mutated_text = mutated_text[:i] + random.choice(alpha_reduced) +\
            mutated_text[i+1:]

    # output
    print(f'You said: "{orig_text}"')
    print(f'I heard : "{mutated_text}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
