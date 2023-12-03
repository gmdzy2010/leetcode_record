def convert(string, row):
    substring_list = []
    for index in range(0, len(string), 2 * row - 2):
        unit = string[index:index + (2 * row - 2)]
        temp = ''.join(c + ' ' * (row - 2) for c in unit[(row - 1):])
        substring = unit[:row - 1] + temp
        substring_list.append(substring)
    new_string = ''.join(substring_list)
    result = '\n'.join(new_string[i::row] for i in range(row))
    return result


if __name__ == '__main__':
    string = "ABCDFASEFASDQWFSDFRWFSDABCDFASEFASDQWFSDFRWFSDABCDFASEFASDQWFSDF"
    result = convert(string, 8)
    print(result)
