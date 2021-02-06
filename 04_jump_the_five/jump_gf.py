#!/usr/bin/env python3

import argparse


# --------------------------------------------------
def get_args():
    """Make the program able to take command-line arguments."""
    parser = argparse.ArgumentParser(
        description='Jump the five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here."""
    args = get_args()
    input_text = args.text

    enc_dict = {'1': 'one ', '2': 'two ', '3': 'three ', '4': 'four ', '5': 'five ',
                '6': 'six ', '7': 'seven ', '8': 'eight ', '9': 'nine ', '10': 'ten '}

    output = ''.join([enc_dict.get(letter, letter) for letter in input_text])
    print(output)


# --------------------------------------------------
if __name__ == '__main__':
    main()
