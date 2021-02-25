#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-25
Purpose: Finding words which are mapped to 666 in give text file
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Devilish words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.str):
        args.str = open(args.str).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    words = args.str.split()

    # finding all the words mapped to 666 through word2num function
    devilish_words = list(filter(lambda w: word2num(w) == '666', words))

    if devilish_words:
        print('Devilish words in your text:')
        for word in devilish_words:
            print(word)
    else:
        print('Such an innocent text!')


# --------------------------------------------------
def word2num(word: str) -> str:
    """Encode a word after removing non-word characters.
    Ex: "Don't" -> "Dont" -> '405'."""

    # remove non-alphabetic chars from the given word
    cleaned_word = re.sub('[^a-zA-Z0-9]', '', word)

    return str(sum(map(ord, cleaned_word)))


# --------------------------------------------------
def test_word2num():
    """Test word2num function"""
    assert word2num("a") == "97"
    assert word2num("abc") == "294"
    assert word2num("ab'c") == "294"
    assert word2num("4a-b'c") == "346"


# --------------------------------------------------
if __name__ == '__main__':
    main()
