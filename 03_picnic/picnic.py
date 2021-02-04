#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-02-03
Purpose: List for a picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('food',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    parser.add_argument('-nc',
                         '--nocomma',
                         help='Eliminate the Oxford comma',
                         action='store_true')
     
    parser.add_argument('-sep',
                        '--separator',
                        metavar='str', 				                        
                        help='User-defined separator',
                        type=str,
                        default=',') 

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    # getting the command-line arguments
    args = get_args()
    foods = args.food
    sep = args.separator
        
    if args.sorted: foods.sort();
    
    # building the output string
    l = len(foods)
    bringings = ''
    if l == 1:
        bringings = foods[0]
    elif l == 2:
        bringings = ' and '.join(foods)
    else:
        bringings = f'{sep} '.join(foods[:-1]) + f'{sep} ' 
        if args.nocomma:
            bringings = bringings[:-2] + ' '             
        bringings += f"and {foods[-1]}"	
    
    print(f"You are bringing {bringings}.")


# --------------------------------------------------
if __name__ == '__main__':
    main()
