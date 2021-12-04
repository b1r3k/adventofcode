import sys
from typing import List


class Board:
    def __init__(self, board: List[List[int]]):
        self._marks = {}
        self.rows = board
        self.max_dim = len(board)

    def mark_number(self, number):
        for row_idx in range(self.max_dim):
            for col_idx in range(self.max_dim):
                if number == self.rows[row_idx][col_idx]:
                    self._marks[row_idx, col_idx] = True
                    yield row_idx, col_idx

    def _get_column_marks(self, col_idx):
        for row_idx in range(self.max_dim):
            yield self._marks.get((row_idx, col_idx), False)

    def _get_row_marks(self, row_idx):
        for col_idx in range(self.max_dim):
            yield self._marks.get((row_idx, col_idx), False)

    def is_winning_row(self, row_idx):
        marks = list(self._get_row_marks(row_idx))
        print(marks)
        return all(marks)

    def is_winning_column(self, col_idx):
        return all(self._get_column_marks(col_idx))

    def get_unmarked_numbers(self):
        for row_idx in range(0, len(self.rows[0])):
            for col_idx in range(0, len(self.rows[0])):
                if not self._marks.get((row_idx, col_idx), False):
                    yield self.rows[row_idx][col_idx]


def solution(winning_numbers, boards):
    nice_boards = list(Board(board) for board in boards)
    for winning_number in winning_numbers:
        print('Checking for winning number: ', winning_number)
        for board_idx, board in enumerate(nice_boards):
            for has_number in board.mark_number(winning_number):
                row_idx, col_idx = has_number
                print(f'{winning_number} is in row {row_idx} and column {col_idx} on board {board_idx}')
                has_winning_column = board.is_winning_column(col_idx)
                has_winning_row = board.is_winning_row(row_idx)
                if has_winning_column or has_winning_row:
                    print(f'Board {board_idx} is a winner! Column: {has_winning_column} Row: {has_winning_row}')
                    unmarked_sum = sum(board.get_unmarked_numbers())
                    return winning_number * unmarked_sum


def read_board(lines):
    board = []
    for line in fd:
        line = line.strip()
        if line:
            try:
                integers = filter(lambda item: len(item), [item.strip() for item in line.split(' ')])
                board_row = list(map(lambda x: int(x), integers))
                board.append(board_row)
            except ValueError:
                raise ValueError(line, integers)
        else:
            return board


def read_input(fd):
    boards = []
    board = []
    winning_numbers = list(map(lambda x: int(x), fd.readline().split(',')))
    fd.readline()
    raw_boards = fd.readlines()
    for line in raw_boards:
        if line[0] != '\n':
            integers = filter(lambda item: len(item), [item.strip() for item in line.split(' ')])
            board_row = list(map(lambda x: int(x), integers))
            board.append(board_row)
        else:
            boards.append(board)
            board = []
    if len(board):
        boards.append(board)
    # print('Boards: ', len(boards))
    # print('Boards: ', boards)
    return winning_numbers, boards


if __name__ == '__main__':
    with open('test_input.txt', 'r') as f:
        data = read_input(f)
    test_data_solution = solution(*data)
    assert test_data_solution == 4512, f'invalid response ({test_data_solution}) to test data'
    data = read_input(sys.stdin)
    print(solution(*data))
