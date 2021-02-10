def remove_element_standard_lib(sequence, value):
    """The way of using standard library."""
    while value in sequence:
        sequence.remove(value)
    return len(sequence)


def remove_element_direct(sequence, value):
    index, length = 0, len(sequence)
    while index < length:
        if sequence[index] == value:
            for second_index in range(index + 1, length):
                sequence[second_index - 1] = sequence[second_index]
                
            # shorten sequence (inplace) and length.
            sequence[:] = sequence[:-1]
            length -= 1
            
            # retreat the index to avoid jump the element neighboured
            index -= 1
        index += 1
    return len(sequence)


def remove_element_double_pointer(sequence, value):
    pass


if __name__ == '__main__':
    test_sequence = [1, 2, 4, 3, 4, 6, 4, 9]
    # result = remove_element_standard_lib(test_sequence, 4)
    result = remove_element_direct(test_sequence, 4)
    # result = remove_element_double_pointer(test_sequence, 4)
    print(result)
