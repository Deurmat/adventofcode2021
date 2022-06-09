# https://adventofcode.com/2021/day/4

import os
import sys
from typing import Tuple
from unittest import result
sys.path.append(os.getcwd())

from src.modules.aoc_module import get_data_raw

class Board:
    def __init__(self, board: list):
        self.board = []
        self._setup_board(board)

    def _setup_board(self, board):
         for i in board:
             self.board.append([j for j in i.split(' ') if j != ''])

def read_raw_data(data:str)->Tuple[list, list]:
    def generate_moves(data:str)->list:
        return data.splitlines()[0].split(',')

    def generate_boards(data:str)->list:
        SPLIT_DISTANCE = 6
        split_lines = data.splitlines()[1:]
        # board_amount = int((len(split_lines) - 1) / SPLIT_DISTANCE)
      
        split_points = [i for i in range(0, len(split_lines), SPLIT_DISTANCE)]

        boards = [split_lines[i+1:i+SPLIT_DISTANCE] for i in split_points]

        result_boards = []
        for board in boards: result_boards.append(Board(board))
        return result_boards
    
    return generate_moves(data), generate_boards(data)

def process_move(move: str, boards: list)-> list:
    pass

def play_moves(moves: list):
    for i in moves: 





if __name__ == "__main__":
    raw_data = get_data_raw('4', 'FILE1')
    moves, boards = read_raw_data(raw_data)

    print(f'MOVES: {moves}, BOARDS: {boards}')
    print(boards[0].board)

