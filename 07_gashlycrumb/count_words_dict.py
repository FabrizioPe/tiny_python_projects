#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-10
Purpose: Counting words in a text using a dictionary
"""

import argparse
from collections import Counter
# from pprint import pprint


# --------------------------------------
def get_args():
    """Get command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Count words in a text file using a dictionary",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('-c',
                        '--common',
                        type=int,
                        metavar='num',
                        help='Print the num most common words',
                        default=10)

    return parser.parse_args()


# --------------------------------------
def main():
    """Make a jazz noise, boy!"""

    args = get_args()
    fh = args.file
    common = args.common

    undesired = [',', '.', ';', '!', '?', '"']
    words = Counter()  # like an empty dictionary
    for line in fh:
        words_in_line = line.split()
        # processing the words a bit: eliminating undesired characters,
        # making words lowercase
        for i in range(len(words_in_line)):
            for c in undesired:
                if c in words_in_line[i]:
                    words_in_line[i] = words_in_line[i].replace(c, '')
        words_in_line = [w.lower() for w in words_in_line]
        words.update(words_in_line)  # counting

    # pprint(words)
    if common:
        print(f"The {common} most common words are:")
        for word, occurr in words.most_common(common):
            print(f'{word:8}', '->', f'{occurr:3}')


# --------------------------------------
if __name__ == '__main__':
    main()
