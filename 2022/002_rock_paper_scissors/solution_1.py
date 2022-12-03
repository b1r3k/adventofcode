import sys


def score_round(move, response):
    rock = 'A'
    paper = 'B'
    scissors = 'C'
    score = 0

    response = response.translate(str.maketrans('XYZ', 'ABC'))

    # print(f'{move} vs {response}')

    # (1 for Rock, 2 for Paper, and 3 for Scissors
    if response == rock:
        score += 1
    elif response == paper:
        score += 2
    elif response == scissors:
        score += 3
    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
    # 0 if you lost, 3 if the round was a draw, and 6 if you won
    if move == response:
        score += 3
    elif response == rock and move == scissors:
        score += 6
    elif response == scissors and move == paper:
        score += 6
    elif response == paper and move == rock:
        score += 6

    return score


def solution(data):
    total_score = 0
    for move, response in data:
        total_score += score_round(move, response)
    return total_score


def read_input(fd):
    lines = fd.readlines()
    for line in lines:
        move, response = line.strip().split()
        yield move, response


if __name__ == '__main__':
    with open('test_input.txt', 'r') as f:
        data = read_input(f)
        test_data_solution = solution(data)
    assert test_data_solution == 15, f'invalid response ({test_data_solution}) to test data'
    data = read_input(sys.stdin)
    print(solution(data))
