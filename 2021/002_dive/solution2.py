import sys


def solution(course):
    depth = 0
    distance = 0
    aim = 0
    for cmd, units in course:
        if cmd == 'forward':
            distance += units
            depth += aim * units
        elif cmd == 'back':
            distance -= units
        elif cmd == 'up':
            aim -= units
        elif cmd == 'down':
            aim += units
    return distance * depth


def read_input(fd):
    course = []
    for line in fd:
        line = line.strip()
        if line:
            cmd, units = line.split(' ')
            course.append((cmd.lower(), int(units)))
    return course


if __name__ == '__main__':
    with open('test_input.txt', 'r') as f:
        sonar_data = read_input(f)
    test_data_solution = solution(sonar_data)
    assert test_data_solution == 900, f'invalid response ({test_data_solution}) to test data'
    sonar_data = read_input(sys.stdin)
    print(solution(sonar_data))
