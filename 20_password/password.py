#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-03-02
Purpose: Password maker ('going further' point 1)
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

    parser.add_argument('-p',
                        '--percentage',
                        metavar='percent',
                        help='Percent. of letters to obfuscate in l33t (interval (0,1])',
                        type=float,
                        default=1.0)

    args = parser.parse_args()

    if not args.l33t and args.percentage != 1.0:
        parser.error(f'You can enforce --percentage '
                     f'only if l33t option is active')

    if args.percentage <= 0 or args.percentage > 1.0:
        parser.error("--percentage must be in (0, 1]")

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    # extract the words from all the given files; clean and title-case them
    words = {clean(word).title() for fh in args.file for line in fh for word in line.lower().split()}

    # lambda for the length filter (see next for loop)
    right_length = lambda word: args.min_word_len <= len(word) <= args.max_word_len

    passwords = []
    for _ in range(args.num):
        # choose args.num_words words of appropriate length to make up the passwords
        chosen_words = random.sample(list(filter(right_length, sorted(words))), args.num_words)
        passwords.append(''.join([word for word in chosen_words]))

    # obfuscate the passwords if l33t option is present
    if args.l33t:
        passwords = list(map(lambda word: l33t(word, percent=args.percentage), passwords))

    for password in passwords:
        print(password)


# --------------------------------------------------
def clean(word: str) -> str:
    """Remove non-word characters from word"""
    return re.sub(r'\W', '', word)


# --------------------------------------------------
def ransom(word: str, percent: float) -> str:
    """Randomly capitalize percent letters in word"""

    ransom_word = []
    for letter in word:
        if random.uniform(0, 1) <= percent:
            ransom_word.append(letter.upper() if random.choice([0, 1])
                               else letter.lower())
        else:
            ransom_word.append(letter)

    return ''.join(ransom_word)


# --------------------------------------------------
def l33t(text: str, percent: float) -> str:
    """Obfuscate given text :)"""

    table = {'a': '@', 'A': '4', 'O': '0', 't': '+',
             'E': '3', 'I': '1', 'S': '5'}

    def table_sub(letter):
        if letter in table.keys() and random.uniform(0, 1) <= percent:
            return table.get(letter)
        return letter

    return ''.join(map(table_sub, ransom(text, percent))) + random.choice(string.punctuation)


# --------------------------------------------------
if __name__ == '__main__':
    main()
