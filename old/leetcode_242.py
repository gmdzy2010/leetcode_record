def is_anagram_standard_lib(string_1, string_2):
    return sorted(list(string_1)) == sorted(list(string_2))


def is_anagram_hash_array(string_1, string_2):
    record = [0] * 26
    for character in string_1:
        record[ord(character) - 97] += 1
    for character in string_2:
        record[ord(character) - 97] -= 1
    for n in record:
        if n != 0:
            return False
    return True


if __name__ == '__main__':
    test_string_1, test_string_2 = 'ate', 'tee'
    print(is_anagram_hash_array(test_string_1, test_string_2))
