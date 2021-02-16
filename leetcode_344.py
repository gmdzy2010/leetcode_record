def reverse_string_standard_lib(string):
    string[:] = string[::-1]
    return string


def reverse_string_swap(string):
    i, j = 0, len(string) - 1
    while i < j:
        string[i], string[j] = string[j], string[i]
        i += 1
        j -= 1
    return string


if __name__ == '__main__':
    print(reverse_string_standard_lib(['h', 'e', 'l', 'l', '0']))
    print(reverse_string_swap(['h', 'e', 'l', 'l', '0']))
