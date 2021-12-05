import sys
from typing import List


class Map:
    def __init__(self):
        self.map = {}

    @staticmethod
    def get_vertical_points(x1, y1, x2, y2):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            yield x, y1

    @staticmethod
    def get_horizontal_points(x1, y1, x2, y2):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            yield x1, y

    def add_point(self, x, y):
        count = self.map.get((x, y), 0)
        self.map[x, y] = count + 1

    def add_line(self, x1, y1, x2, y2):
        if x1 == x2:
            for x, y in self.get_horizontal_points(x1, y1, x2, y2):
                self.add_point(x, y)
                # print(f'Vertical: {x}, {y}')
        elif y1 == y2:
            for x, y in self.get_vertical_points(x1, y1, x2, y2):
                self.add_point(x, y)
                # print(f'Horizontal: {x}, {y}')

    def get_danger_areas_count(self, danger_level):
        count = 0
        for danger_lvl in self.map.values():
            if danger_lvl >= danger_level:
                count += 1
        return count


def solution(data):
    map = Map()
    for x1, y1, x2, y2 in data:
        map.add_line(x1, y1, x2, y2)
    return map.get_danger_areas_count(2)


def read_input(fd):
    for line in fd:
        line = line.strip()
        x1y1, x2y2 = line.split(' -> ')
        x1, y1 = x1y1.split(',')
        x2, y2 = x2y2.split(',')
        yield int(x1), int(y1), int(x2), int(y2)


if __name__ == '__main__':
    with open('test_input.txt', 'r') as f:
        data = read_input(f)
        test_data_solution = solution(data)
    assert test_data_solution == 5, f'invalid response ({test_data_solution}) to test data'
    data = read_input(sys.stdin)
    print(solution(data))
