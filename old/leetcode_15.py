def three_number_sum_double_pointer(sequence):
    length, result = len(sequence), []
    
    # It's necessary to inplace sort the original sequence to use the
    # double-pointer scan way.
    sequence.sort()
    
    # Start scan use left, middle and right index.
    for left_i in range(length):
        # Stop the left index loop when the most left element of the sorted
        # sequence is larger than 0.
        if sequence[left_i] > 0:
            break
        
        # Duplicate removal.
        if left_i > 0 and sequence[left_i] == sequence[left_i - 1]:
            continue
        
        right_i, target = length - 1, -sequence[left_i]
        for middle_i in range(left_i + 1, length):
            # Combined with code of line 5 to deal with the situation of
            # continuously appear the same element.
            if middle_i > left_i + 1 \
                    and sequence[middle_i] == sequence[middle_i - 1]:
                continue
            
            # Retreat right index if sum of elements on the middle index and
            # right index is larger than the one on the left index.
            while middle_i < right_i \
                    and sequence[middle_i] + sequence[right_i] > target:
                right_i -= 1
            
            # stop the for loop when middle index meets the right index.
            if middle_i >= right_i:
                break
            
            # Store answer.
            if sequence[middle_i] + sequence[right_i] == target:
                result.append(
                    [sequence[left_i], sequence[middle_i], sequence[right_i]])
    return result


if __name__ == '__main__':
    test_sequence = [-1, 0, 1, 2, 2, 2, 2, -1, -1, -4, 3, 4, 7]
    test_result = three_number_sum_double_pointer(test_sequence)
    print(test_result)
