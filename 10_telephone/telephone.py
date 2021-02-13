#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-13
Purpose: Reproducing the "telephone" game: 'going further' section
Notes: I didn't include new tests because I couldn't see how to determine the
       expected output without actually writing the code, which would make
       the tests itself useless (self-referential).
"""

import argparse
import os
import random
import string
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Randomly mutate, insert, delete letters in a given text ',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations in each word',
                        metavar='mutations',
                        type=float,
                        default=0.4)

    parser.add_argument('-i',
                        '--insertions',
                        help='Percent insertions in each word',
                        metavar='insertions',
                        type=float,
                        default=0)

    parser.add_argument('-d',
                        '--deletions',
                        help='Percent deletions in each word',
                        metavar='deletions',
                        type=float,
                        default=0)

    parser.add_argument('-w',
                        '--words',
                        help='Percent of words to mutate',
                        metavar='words_mutations',
                        type=float,
                        default=0.5)

    parser.add_argument('-np',
                        '--no_punct',
                        help='Leave punctuation unaltered',
                        action='store_true')

    parser.add_argument('-o',
                        '--output',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if not 0 <= args.words <= 1:
        parser.error(f'--words "{args.words}" must be between 0 and 1')

    if not 0 <= args.insertions <= 1:
        parser.error(f'--insertions "{args.insertions}" must be between 0 and 1')

    if not 0 <= args.deletions <= 1:
        parser.error(f'--deletions "{args.deletions}" must be between 0 and 1')

    if os.path.isfile(args.text):
        args.text = open(args.text).read()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    orig_text = args.text.strip()
    mutations = args.mutations
    insertions = args.insertions
    deletions = args.deletions
    words_mutations = args.words
    no_punct = args.no_punct
    output_fh = args.output
    random.seed(args.seed)

    # determining the characters to use
    if no_punct:
        alpha = ''.join(sorted(string.ascii_letters))
    else:
        alpha = ''.join(sorted(string.ascii_letters + string.punctuation))

    words = orig_text.split()
    words_ind = random.sample(range(len(words)), round(words_mutations * len(words)))
    # iterate over the selected words of the original text, to mutate them
    for i in words_ind:
        letters = list(words[i])  # split the current word in a list
        num_mutations = round(mutations * len(letters))
        indexes = random.sample(range(len(letters)), num_mutations)
        for j in indexes:  # mutate the letters in the current word
            if no_punct and letters[j] in string.punctuation:
                continue
            letters[j] = random.choice(alpha.replace(letters[j], ''))
        if insertions:  # insert random letters at the indicated frequency
            num_insertions = round(insertions * len(letters))
            for _ in range(num_insertions):
                ind_insertions = random.choice(range(len(letters)))
                if no_punct and letters[ind_insertions] in string.punctuation:
                    continue
                letters.insert(ind_insertions, random.choice(alpha))
        if deletions:  # delete random letters at the indicated frequency
            num_deletions = round(deletions * len(letters))
            for _ in range(num_deletions):
                ind_deletions = random.choice(range(len(letters)))
                if no_punct and letters[ind_deletions] in string.punctuation:
                    continue
                del letters[ind_deletions]

        words[i] = ''.join(letters)  # aggregate the letters in a word again
    mutated_text = ' '.join(words)

    # output
    print(f'You said: "{orig_text}"', file=output_fh)
    print(f'I heard : "{mutated_text}"', file=output_fh)
    print(f'The process has mutated words {sorted(words_ind)}', file=output_fh)
    output_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
