import sys


def solution(data):
    increasing_measurements_count = 0
    for reading_idx in range(1, len(data)):
        if data[reading_idx] > data[reading_idx - 1]:
            increasing_measurements_count += 1
    return increasing_measurements_count


def read_input(fd):
    sonar_data = []
    for line in fd:
        line = line.strip()
        if line:
            sonar_data.append(int(line))
    return sonar_data


if __name__ == '__main__':
    with open('test_input.txt', 'r') as f:
        sonar_data = read_input(f)
    test_data_solution = solution(sonar_data)
    assert test_data_solution == 7, f'invalid response ({test_data_solution}) to test data'
    sonar_data = read_input(sys.stdin)
    print(solution(sonar_data))
