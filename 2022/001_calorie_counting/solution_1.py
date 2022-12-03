import sys


def transform_input(data):
    calorie_stack = []
    for line in data.splitlines():
        if line in '\n ':
            yield calorie_stack
            calorie_stack = []
        else:
            calorie_stack.append(int(line.strip()))

    if calorie_stack:
        yield calorie_stack


def solution(data):
    max_calories = 0

    for elf_stack in transform_input(data):
        calories = sum(elf_stack)
        if calories > max_calories:
            max_calories = calories

    return max_calories


def read_input(fd):
    data = fd.read()
    return data


if __name__ == '__main__':
    with open('test_input.txt', 'r') as f:
        data = read_input(f)
        test_data_solution = solution(data)
    assert test_data_solution == 24000, f'invalid response ({test_data_solution}) to test data'
    data = read_input(sys.stdin)
    print(solution(data))
