def reverse_int(x):
    if x >= 0:
        number = int("".join(list(str(x))[::-1]))
        return number if number <= pow(2, 31) - 1 else 0
    else:
        number = int("".join(list(str(x).replace("-", ""))[::-1]))
        return - number if number < pow(2, 31) else 0


if __name__ == '__main__':
    print(reverse_int(19292991))
