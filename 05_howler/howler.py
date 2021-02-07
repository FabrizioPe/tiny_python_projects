#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-06
Purpose: Read input and make it upper[lower]case (optionally, print the
         output to a specified directory). This is the 'going further' version
         of the program.
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper[lower]-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str_or_file',
                        metavar='text',
                        type=str,
                        nargs='+',
                        help='Input string or file')

    parser.add_argument('-e',
                        '--ee',
                        help='Lower-cases input',
                        action='store_true')

    parser.add_argument('-o',
                        '--outdir',
                        metavar='dir',
                        help='Output directory',
                        type=str,
                        default='.')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    input_str = args.str_or_file
    out_dir = args.outdir

    # process input (create upper or lower case text)
    for item in input_str:
        if os.path.isfile(item):
            with open(item) as in_fh:
                input_text = in_fh.read()
        else:
            input_text = item
        if args.ee: input_text = input_text.lower();
        else: input_text = input_text.upper()

    # decide whether print output to stdout or to a file in spec. directory
        if not os.path.isfile(item):
            print(input_text)
        else:
            with open(f'{out_dir}/{os.path.basename(item)}', 'w') as out_fh:
                out_fh.write(input_text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
