def reverse_part_string(string, k):
    length, result = len(string), ''
    for index in range(0, length, 2 * k):
        sub_string = string[index:index + 2 * k]
        result += sub_string[:k][::-1] + sub_string[k:]
    return result


if __name__ == '__main__':
    test_string = 'abcdefg'
    print(reverse_part_string(test_string, 2))
