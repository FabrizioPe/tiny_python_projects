#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-23
Purpose: Mad Libs
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad Libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs (for testing)',
                        metavar='input',
                        type=str,
                        nargs='*')

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.file.read().strip()
    words = args.inputs

    # check the presence of placeholders <...> in text
    match = re.findall('(<([^<>]+)>)', text)
    if not match:
        sys.exit(f'"{args.file.name}" has no placeholders.')

    # prompt user to enter substitution words if not already given
    if not words:
        words = words_to_substitute(match)

    # substitute the words in the given text
    for placeholder, _ in match:
        text = re.sub(placeholder, words.pop(0), text, count=1)

    print(text)


# --------------------------------------------------
def words_to_substitute(match):
    """Ask the user for the words to substitute to placeholders"""
    words = list()
    for _, name in match:
        article = 'an' if name[0].lower() in 'aeiou' else 'a'
        words.append(input(f'Give me {article} {name}: '))

    return words


# --------------------------------------------------
def test_words_to_substitute():
    assert len(words_to_substitute([('<noun>', 'noun'),
                                    ('<article>', 'article')])) == 2
    assert isinstance(words_to_substitute([('<noun>', 'noun'),
                                           ('<article>', 'article')]), list)


# --------------------------------------------------
if __name__ == '__main__':
    main()
