import sys


def get_gamma_rate(reports):
    total_rows = len(reports)
    zero_bits_counter = [0] * len(reports[0])
    most_common_bit = []
    for report in reports:
        for col_idx, col in enumerate(report, start=0):
            if col == '0':
                zero_bits_counter[col_idx] += 1
    for zero_bits_counter_per_col in zero_bits_counter:
        one_bits_counter = total_rows - zero_bits_counter_per_col
        if zero_bits_counter_per_col > one_bits_counter:
            most_common_bit.append('0')
        else:
            most_common_bit.append('1')
    return ''.join(most_common_bit)


def invert_bits(bits):
    inverted_bits = []
    for bit in bits:
        if bit == '0':
            inverted_bits.append('1')
        else:
            inverted_bits.append('0')
    return ''.join(inverted_bits)


def solution(reports):
    gamma_rate_bin = get_gamma_rate(reports)
    gamma_rate = int(gamma_rate_bin, 2)
    epsilon_rate = int(invert_bits(gamma_rate_bin), 2)
    # print(epsilon_rate, gamma_rate, gamma_rate_bin)
    return epsilon_rate * gamma_rate


def read_input(fd):
    data = []
    for line in fd:
        line = line.strip()
        if line:
            data.append(line)
    return data


if __name__ == '__main__':
    with open('test_input.txt', 'r') as f:
        data = read_input(f)
    test_data_solution = solution(data)
    assert test_data_solution == 198, f'invalid response ({test_data_solution}) to test data'
    data = read_input(sys.stdin)
    print(solution(data))
