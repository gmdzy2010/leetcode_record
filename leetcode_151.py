def reverse_words_standard_lib(string):
    return ' '.join([w.replace(" ", "") for w in string.split(" ") if w][::-1])


def reverse_words_swap(string):
    w_list = [word.replace(" ", "") for word in string.split(" ") if word]
    start, end = 0, len(w_list) - 1
    while start < end:
        w_list[start], w_list[end] = w_list[end], w_list[start]
        start += 1
        end -= 1
    return ' '.join(w_list)


if __name__ == '__main__':
    test_string = "  hello world  "
    print(reverse_words_standard_lib(test_string))
    print(reverse_words_swap(test_string))
