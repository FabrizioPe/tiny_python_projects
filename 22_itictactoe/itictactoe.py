#!/usr/bin/env python3
"""
Author : FabrizioPe
Date   : 2021-03-04
Purpose: Interactive tic tac toe game
"""

from typing import NamedTuple, List, Optional
import re


# --------------------------------------------------
class State(NamedTuple):
    """Class that represents the current state of the game.
       It practically is a named tuple with type hints."""
    board: List[str] = list('.' * 9)
    player: str = 'X'
    quit: bool = False
    error: Optional[str] = None
    draw: bool = False
    winner: Optional[str] = None
    repeat: bool = True


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    state = State()
    while state.repeat and not state.quit:
        # i can't really understand why state = State() is not sufficient to
        # clear the state: the board remains the last of the previous game
        state = State(board=list('.' * 9))

        while not any([state.winner, state.draw]):
            print("\033[H\033[J", end='')  # \033 ASCII escape sequence
            print(format_board(state.board))

            if state.error:
                print(state.error)
            if state.quit:
                print("\033[H\033[J", end='')
                break

            state = get_move(state)

            if state.winner:
                print(f"{state.winner} has won!")
            elif state.draw:
                print('This is a draw.')

        if state.quit:
            break

        if play_again() == 'n':
            print("\033[H\033[J", end='')
            state = state._replace(repeat=False)


# --------------------------------------------------
def format_board(board: List[str]) -> str:
    """Return the board formatted for output"""

    out_board = ''
    for i in range(0, len(board)):
        if i == 0 or i % 3 == 0:
            out_board += '\n' + '-------------' + '\n|'
        tic = board[i] if board[i] in 'XO' else i + 1
        out_board += f' {tic} |'
    out_board += '\n' + '-' * 13

    return out_board.strip()


# --------------------------------------------------
def find_winner_or_draw(state: State) -> State:
    """Check if there's a winner and who is, or if it's a draw"""

    winning_boards = ['PPP......', '...PPP...', '......PPP', 'P..P..P..',
                      '.P..P..P.', '..P..P..P', 'P...P...P', '..P.P.P..']

    board = ''.join(state.board)
    for player in 'XO':
        for wb in winning_boards:
            player_wb = wb.replace('P', player)
            if re.match(player_wb, board):
                return state._replace(winner=player)

    if '.' not in board:
        return state._replace(draw=True)

    return state


# --------------------------------------------------
def get_move(state: State) -> State:
    """Get next move, check if it's legitimate.
       If it's not, record the error or the quit choice.
       Otherwise, update the board and determine if
       there's a winner or a draw."""

    new_move = input(f'Player {state.player}, what is your move? [q to quit]: ')

    if new_move == 'q':
        state = state._replace(quit=True)

    elif new_move not in list('123456789'):
        state = state._replace(error=f'Invalid cell "{new_move}", please use 1-9')

    elif state.board[int(new_move) - 1] in 'XO':
        state = state._replace(error=f'Cell "{new_move}" already taken')

    else:
        new_board = state.board
        new_board[int(new_move) - 1] = state.player
        state = state._replace(board=new_board,
                               player={'X', 'O'}.difference(state.player).pop(),
                               error=None)
        state = find_winner_or_draw(state)

    return state


# --------------------------------------------------
def play_again() -> str:
    """Ask the user if he wants to play another turn"""

    yes_or_no = input('Play again? [y/n]: ')
    while yes_or_no not in ['y', 'n']:
        yes_or_no = input('Please insert "y" or "n": ')

    return yes_or_no


# --------------------------------------------------
if __name__ == '__main__':
    main()
