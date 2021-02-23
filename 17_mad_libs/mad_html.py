#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-23
Purpose: Find all HTML tags enclosed in <...> and </...> in a web page
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find html tags',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

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

    candidate_tags = re.findall('<([^!/]+?)>', text)
    real_tags = [tag for tag in candidate_tags if re.search(f'</{tag}>', text)]

    if not real_tags:
        sys.exit("This doesn't look like an html page")

    print('The page contains the following tags:')
    for tag in real_tags:
        print(tag)


# --------------------------------------------------
if __name__ == '__main__':
    main()
