import sys


def get_most_common_bits(reports):
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


def filter_reports_by_bit_criteria(reports, bit_criteria, bit_idx):
    for report in reports:
        if report[bit_idx] == bit_criteria[bit_idx]:
            yield report


def get_report_by_bit_criteria(reports, bit_criteria_func):
    filtered_reports = reports
    bit_idx = 0
    while len(filtered_reports) > 1:
        most_common_bits = bit_criteria_func(filtered_reports)
        filtered_reports = list(filter_reports_by_bit_criteria(filtered_reports, most_common_bits, bit_idx))
        # print(f'{bit_idx}: {filtered_reports}')
        bit_idx += 1
    return filtered_reports[0]


def invert_bits(bits):
    inverted_bits = []
    for bit in bits:
        if bit == '0':
            inverted_bits.append('1')
        else:
            inverted_bits.append('0')
    return ''.join(inverted_bits)


def solution(reports):
    oxygen_gen_rating_bin = get_report_by_bit_criteria(reports, get_most_common_bits)
    co2_scrubber_rating_bin = get_report_by_bit_criteria(reports, lambda r: invert_bits(get_most_common_bits(r)))
    oxygen_gen_rating = int(oxygen_gen_rating_bin, 2)
    co2_scrubber_rating = int(co2_scrubber_rating_bin, 2)
    # print('Oxygen generator rating: {} {}'.format(oxygen_gen_rating, oxygen_gen_rating_bin))
    # print('CO2 scrubber rating: {} {}'.format(co2_scrubber_rating, co2_scrubber_rating_bin))
    return oxygen_gen_rating * co2_scrubber_rating


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
    assert test_data_solution == 230, f'invalid response ({test_data_solution}) to test data'
    data = read_input(sys.stdin)
    print(solution(data))
