#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-19
Purpose: Transforming a given text in a deep-US-sounding text, i.e.
         admiring -> admirin', you -> y'all
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Southern fry text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.str):
        args.str = open(args.str).read().strip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.str
    lines = text.splitlines()  # split the text by lines
    for line in lines:
        # each line is splitted in words according to non-word characters;
        # then, fry is applied to each word.
        print(''.join(map(fry, re.split(r'(\W+)', line))))


# --------------------------------------------------
def fry(word: str):
    """Ex: you -> y'all, cooking -> cookin', swing -> swing,
    wardrobe -> wardrobe"""

    if re.match('[Yy]ou$', word):
        return word[0] + "'all"

    match = re.search("(.+)ing$", word)  # check if word ends by 'ing'
    if match and re.search('[aeiou]', match.group(1)):  # check if it's a 2 syllables word
        return match.group(1) + "in'"
    else:
        # it's a 1 syllable word or a 'you' or 'ing'-ending word:
        # return the word unchanged
        return word


# --------------------------------------------------
def test_fry():
    assert fry('you') == "y'all"
    assert fry('You') == "Y'all"
    assert fry('Admiring') == "Admirin'"
    assert fry('cooking') == "cookin'"
    assert fry('swing') == "swing"
    assert fry('Microphone') == 'Microphone'


# --------------------------------------------------
if __name__ == '__main__':
    main()
