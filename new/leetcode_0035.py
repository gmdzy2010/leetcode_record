# Direct way, time: O(n)
def search_insert_direct(sequence, target):
    """The direct way."""
    for index, num in enumerate(sequence):
        if sequence[index] >= target:
            return index
    return len(sequence)


# Dichotomy way
def search_insert_dichotomy(sequence, target):
    left, right = 0, len(sequence) - 1
    while left <= right:
        middle = (left + right) // 2
        if target < sequence[middle]:
            right = middle - 1
        elif sequence[middle] == target:
            return middle
        else:
            left = middle + 1
    return right + 1


if __name__ == '__main__':
    test_sequence = [1, 3, 4, 5, 6, 9]
    test_target = 7
    result_1 = search_insert_direct(test_sequence, test_target)
    result_2 = search_insert_dichotomy(test_sequence, test_target)
    print(result_1, result_2)
