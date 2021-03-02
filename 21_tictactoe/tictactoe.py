#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-03-02
Purpose: Implementation of one move of 'tictactoe' game
"""

import argparse
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                        '--board',
                        help='The state of the board',
                        metavar='str',
                        type=str,
                        default='.' * 9)

    parser.add_argument('-p',
                        '--player',
                        help='Player',
                        metavar='str',
                        type=str,
                        choices='XO',
                        default=None)

    parser.add_argument('-c',
                        '--cell',
                        help='Cell 1-9',
                        metavar='int',
                        type=int,
                        choices=range(1, 10),
                        default=None)

    args = parser.parse_args()

    if not re.match(r'^[.XO]{9}$', args.board):
        parser.error(f'--board "{args.board}" must be 9 characters of ., X, O')

    # should've used any and all here
    if (not args.player and args.cell) or (args.player and not args.cell):
        parser.error("Must provide both --player and --cell")

    if args.cell and args.board[args.cell - 1] in 'XO':
        parser.error(f'--cell "{args.cell}" already taken')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    board = args.board

    # modify the board with the move of the player
    if args.player:
        board = board[:args.cell - 1] + args.player + board[args.cell:]

    print(format_board(board))
    winner = find_winner(board)
    print(f'{winner} has won!' if winner else 'No winner.')

# --------------------------------------------------
def format_board(board: str) -> str:
    """Return the board formatted for output"""

    out_board = ''
    for i in range(0, len(board)):
        if i == 0 or i % 3 == 0:
            out_board += '\n' + '-------------' + '\n|'
        tic = board[i] if board[i] in 'XO' else i + 1
        out_board += f' {tic} |'
    out_board += '\n' + '-' * 13

    return out_board.lstrip()


# --------------------------------------------------
def find_winner(board: str):
    """Check if there's a winner and who is"""

    winning_boards = ['PPP......', '...PPP...', '......PPP', 'P..P..P..',
                      '.P..P..P.', '..P..P..P', 'P...P...P', '..P.P.P..']

    for player in 'XO':
        for wb in winning_boards:
            player_wb = wb.replace('P', player)
            if re.match(player_wb, board):
                return player

    return None


# --------------------------------------------------
if __name__ == '__main__':
    main()
