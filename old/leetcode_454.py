def four_number_sum_counts_hash_map(
        sequence_a, sequence_b, sequence_c, sequence_d):
    sum_ab_counts = {}
    for a in sequence_a:
        for b in sequence_b:
            if a + b in sum_ab_counts:
                sum_ab_counts[a + b] += 1
            else:
                sum_ab_counts[a + b] = 1
    sum_abcd_0_count = 0
    for c in sequence_c:
        for d in sequence_d:
            if -(c + d) in sum_ab_counts:
                sum_abcd_0_count += sum_ab_counts[-(c + d)]
    return sum_abcd_0_count


if __name__ == '__main__':
    test_a = [1, 2]
    test_b = [-2, -1]
    test_c = [-1, 2]
    test_d = [0, 2]
    print(four_number_sum_counts_hash_map(test_a, test_b, test_c, test_d))
