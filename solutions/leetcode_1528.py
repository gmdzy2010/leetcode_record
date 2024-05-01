def restoreString(s, indices):
    result = [(index, char) for index, char in zip(indices, s)]
    result = sorted(result, key=lambda x: x[0])
    final = ''.join(char for _, char in result)
    return final


if __name__ == '__main__':
    string, indices = 'codeleet', [4,5,6,7,0,2,1,3]
    final = restoreString(string, indices)
    print(final)
