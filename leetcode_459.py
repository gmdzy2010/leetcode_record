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
            prefix_index = prefix_table[prefix_index - 1]
        else:
            suffix_index += 1
    return prefix_table


def repeated_substring_pattern(string):
    length, prefix_table = len(string), get_prefix_table(string)
    
    # The length of max public string of prefix and suffix.
    max_length_public_pre_suf = length - prefix_table[-1]
    if length % max_length_public_pre_suf == 0 and prefix_table[-1] != 0:
        return True
    return False


if __name__ == '__main__':
    print(repeated_substring_pattern("asdfasdfasdf"))
