def get_first_position_standard_lib(string, pattern):
    return string.find(pattern)


def get_prefix_table(pattern):
    length = len(pattern)
    prefix_table = [0] * length
    prefix_index, suffix_index = 0, 1
    while suffix_index < length:
        if pattern[suffix_index] == pattern[prefix_index]:
            prefix_table[suffix_index] = prefix_index + 1
            prefix_index += 1
            suffix_index += 1
        elif prefix_index > 0:
            
            # Move backward step by step rather than jump directly to 0.
            prefix_index = prefix_table[prefix_index - 1]
        else:
            suffix_index += 1
    return prefix_table


def get_first_position_kmp(string, pattern):
    string_length, pattern_length = len(string), len(pattern)
    if pattern_length == 0:
        return 0
    prefix_table = get_prefix_table(pattern)
    string_index = pattern_index = 0
    while string_index < string_length:
        
        # Partial match, increase string/pattern index.
        if string[string_index] == pattern[pattern_index]:
            
            # Totally match the pattern string, stop search.
            if pattern_index == pattern_length - 1:
                return string_index - pattern_index
            
            string_index += 1
            pattern_index += 1
        
        # Move backwards based on the prefix table
        elif pattern_index > 0:
            pattern_index = prefix_table[pattern_index - 1]
        else:
            string_index += 1
    return -1


if __name__ == '__main__':
    print(get_prefix_table("abababab"))
    print(get_first_position_kmp('hello', 'll'))
