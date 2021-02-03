#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-02
Purpose: choose the correct article according to user input word
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='word', help='A word')  # metavar defines what will appear in the help!
    parser.add_argument('-s', '--starboard', help='Turns "starboard" to "larboard" in the output', action='store_true') 	

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    lar_to_star = args.starboard			
    
    # check if input starts with a letter
    if not word[0].isalpha(): 
        print("What kind of animal is that, you fool?!?")
        return -1
    # processing the input
    if word[0].lower() in 'aeiou':
        article = 'An' if word[0].isupper() else 'an'
    else:
        article = 'A' if word[0].isupper() else 'a'
    side = 'starboard' if lar_to_star else 'larboard'		 	
    print(f"Ahoy, Captain, {article} {word} off the {side} bow!")					

# --------------------------------------------------
if __name__ == '__main__':
    main()
