def min_sub_sequence_len_direct(sequence, target):
    length, min_length = len(sequence), []
    for index_1 in range(length):
        for index_2 in range(index_1, length):
            sub_nums = sequence[index_1:index_2 + 1]
            if sum(sub_nums) >= target:
                min_length.append(len(sub_nums))
    return 0 if not min_length else min(min_length)


def min_sub_sequence_len_sliding_window(sequence, target):
    start_index = end_index = total = 0
    length = len(sequence)
    
    # In order to avoid situation that the answer is equal to length.
    min_sub_length = length + 1
    
    # Keep end index moving forward.
    while end_index < length:
        # Use increasing sum to avoid duplicate sum operation each time.
        total += sequence[end_index]
        
        # Move forward start index when the sum is equal or larger than target.
        # shorten the sliding window in order to detect if a smaller length
        # exists.
        while total >= target:
            current_length = end_index - start_index + 1
            min_sub_length = min(min_sub_length, current_length)
            total -= sequence[start_index]
            start_index += 1
        end_index += 1
    return 0 if min_sub_length == length + 1 else min_sub_length


if __name__ == '__main__':
    test_sequence, test_target = [1, 2, 4, 5, 7, 8], 8
    # result = min_sub_sequence_len_direct(test_sequence, test_target)
    result = min_sub_sequence_len_sliding_window(test_sequence, test_target)
    print(result)
