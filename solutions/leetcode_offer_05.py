def replace_space_standard_lib(string):
    return string.replace(" ", "%20")


def replace_space_double_pointer(string):
    space_count = string.count(" ")
    extended = [None] * (space_count * 2 + len(string))
    left_index, right_index = len(string) - 1, len(extended) - 1
    while left_index >= 0:
        if string[left_index] != " ":
            extended[right_index] = string[left_index]
            right_index -= 1
        else:
            extended[right_index] = '0'
            extended[right_index - 1] = '2'
            extended[right_index - 2] = '%'
            right_index -= 3
        left_index -= 1
    return ''.join(extended)


if __name__ == '__main__':
    import time
    test_string = """
    When Python 2.7 was still supported, a lot of functionality in Python 3
    was kept for backward compatibility with Python 2.7. With the end of Python
    2 support, these backward compatibility layers have been removed, or will
    be removed soon. Most of them emitted a DeprecationWarning warning for
    several years. For example, using collections.Mapping instead of
    collections.abc.Mapping emits a DeprecationWarning since Python 3.3,
    released in 2012.
    """
    # test_string = """I am happy"""
    start_time_1 = time.time()
    result_1 = replace_space_standard_lib(test_string)
    cost_time_1 = time.time() - start_time_1
    
    start_time_2 = time.time()
    result_2 = replace_space_double_pointer(test_string)
    cost_time_2 = time.time() - start_time_2
    
    print("standard_lib_version: {:.5f}".format(cost_time_1))
    print("double_pointer_version: {:.5f}".format(cost_time_2))
