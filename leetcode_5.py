def longest_palindrome_substring(string):
    """The low efficiency version."""
    length, palindromes = len(string), []
    for left_index in range(length + 1):
        for right_index in range(left_index, length + 1):
            substring = string[left_index:right_index]
            if substring and substring == substring[::-1]:
                palindromes.append(substring)
    return max(palindromes, key=lambda x: len(x))


if __name__ == '__main__':
    string = "abcbbbcba"
    print(longest_palindrome_substring(string))
