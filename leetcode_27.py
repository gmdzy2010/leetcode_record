def remove_element_standard_lib(sequence, value):
    """The way of using standard library."""
    while value in sequence:
        sequence.remove(value)
    return len(sequence)


def remove_element_direct(sequence, value):
    pass


def remove_element_double_pointer(sequence, value):
    pass


if __name__ == '__main__':
    test_sequence = [1, 2, 3, 4, 6, 4, 9]
    result = remove_element_standard_lib(test_sequence, 4)
    # result = remove_element_direct(test_sequence, 4)
    # result = remove_element_double_pointer(test_sequence, 4)
