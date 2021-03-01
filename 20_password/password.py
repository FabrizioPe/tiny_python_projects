#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-03-01
Purpose: Password maker
"""

import argparse
import random
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Password maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file(s)',
                        type=argparse.FileType('rt'),
                        nargs='+')

    parser.add_argument('-n',
                        '--num',
                        help='Number of passwords to generate',
                        metavar='num_passwords',
                        type=int,
                        default=3)

    parser.add_argument('-w',
                        '--num_words',
                        help='Number of words to use for password',
                        metavar='num_words',
                        type=int,
                        default=4)

    parser.add_argument('-m',
                        '--min_word_len',
                        help='Minimum word length',
                        metavar='minimum',
                        type=int,
                        default=3)

    parser.add_argument('-x',
                        '--max_word_len',
                        help='Maximum word length',
                        metavar='maximum',
                        type=int,
                        default=6)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-l',
                        '--l33t',
                        help='Obfuscate letters',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    # extract the words from all the given files, and clean them
    words = {clean(word).title() for fh in args.file for line in fh for word in line.lower().split()}

    # lambda for the length filter (see next for)
    right_length = lambda word: args.min_word_len <= len(word) <= args.max_word_len

    passwords = []
    for _ in range(args.num):
        # choose args.num_words words of appropriate length to make up the passwords
        chosen_words = random.sample(list(filter(right_length, sorted(words))), args.num_words)
        passwords.append(''.join([word for word in chosen_words]))

    # obfuscate the passwords if l33t option is present
    if args.l33t:
        passwords = list(map(l33t, passwords))

    for password in passwords:
        print(password)


# --------------------------------------------------
def clean(word: str) -> str:
    """Remove non-word characters from word"""

    return re.sub(r'\W', '', word)


# --------------------------------------------------
def ransom(word: str) -> str:
    """Randomly capitalize letters in word"""

    return ''.join([letter.upper() if random.choice([0, 1]) else
                    letter.lower() for letter in word])


# --------------------------------------------------
def l33t(text: str) -> str:
    """Obfuscate given text"""

    table = {'a': '@', 'A': '4', 'O': '0', 't': '+',
             'E': '3', 'I': '1', 'S': '5'}

    table_sub = lambda letter: table.get(letter, letter)
    return ''.join(map(table_sub, map(ransom, text))) + random.choice(string.punctuation)


# --------------------------------------------------
if __name__ == '__main__':
    main()
