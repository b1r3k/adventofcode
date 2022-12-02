import sys
from typing import List


def solution(data):
    pass


def read_input(fd):
    data = fd.read()
    for n in data.strip().split(','):
        yield int(n)


if __name__ == '__main__':
    with open('test_input.txt', 'r') as f:
        data = read_input(f)
        test_data_solution = solution(data)
    assert test_data_solution == 5934, f'invalid response ({test_data_solution}) to test data'
    data = read_input(sys.stdin)
    print(solution(data))
