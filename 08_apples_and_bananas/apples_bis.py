#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-10
Purpose: Find and replace vowels in a given text, alternative methods
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='str',
                        choices='aeiou',
                        type=str,
                        default='a')

    args = parser.parse_args()

    if os.path.isfile(args.str):
        args.str = open(args.str).read().rstrip()

    return args


# --------------------------------------------------
def vowel_transf(letter):
    # not so efficient memory-wise...
    # but forced to do so by its use in a map.
    # The alternative is to define it inside main, so vowel is in scope
    vowel = get_args().vowel

    return vowel if letter in 'aeiou' \
        else vowel.upper() if letter in 'AEIOU' else letter


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.str
    vowel = args.vowel

    table = {'a': vowel, 'e': vowel, 'i': vowel, 'o': vowel, 'u': vowel,
             'A': vowel.upper(), 'E': vowel.upper(), 'I': vowel.upper(),
             'O': vowel.upper(), 'U': vowel.upper()}

    # ---- 1) ----
    print('1', ''.join([table.get(letter, letter) for letter in text]))
    print('1', ''.join([vowel if letter in 'aeiou' else vowel.upper()
        if letter in 'AEIOU' else letter for letter in text]))

    # ---- 2) ----
    new_text = ''
    for lett in text:
        new_text += lett.replace(lett, table.get(lett, lett))
    print('2', new_text)

    # ---- 3) ----
    new_text2 = map(lambda letter: table[letter] if letter in table else letter, text)
    print('3', ''.join(new_text2))

    # ---- 4) ---- perhaps my favorite
    new_text3 = map(lambda letter: vowel if letter in 'aeiou'
        else vowel.upper() if letter in 'AEIOU'
        else letter, text)
    print('4', ''.join(new_text3))

    # ---- 5) ----
    new_text4 = map(vowel_transf, text)
    print('5', ''.join(new_text4))

    # ---- 'going further' section ----
    # substitution with collapse: "quick" -> "qack", not "qaack"
    new_text5 = ''
    changed = False  # a way to signal that the previous letter is a vowel
    for c in text:
        if c not in 'aeiouAEIOU':
            new_text5 += c
            changed = False
        else:
            if changed:
                new_text5 += ''
            else:
                new_text5 += table[c]
                changed = True

    print('7', new_text5)


# --------------------------------------------------
if __name__ == '__main__':
    main()
