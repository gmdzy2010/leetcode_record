def length_of_longest_substring(string):
    """Learned from LEETCODE."""
    start_index, max_length, record = -1, 0, {}
    for string_index, character in enumerate(string):
        # 我觉得这里“c_dict[c] > k”代表的意思是当前字符串上次出现的位置在这次的考察区间内，
        # 这代表当前字符串已经在之前的统计过程中出现过了，重复了，不符合要求，那么考察区间的
        # 起始位置就得刷新到同一个字符这次出现的位置，作为新的新的考察区间的起始位置。
        if character in record and start_index < record[character]:
            start_index = record[character]
        else:
            max_length = max(max_length, string_index - start_index)
        record[character] = string_index
    return max_length


if __name__ == '__main__':
    string = 'abcabcbb'
    print(length_of_longest_substring(string))
