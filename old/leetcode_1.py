def two_sum(nums, target):
    position = {value: index for index, value in enumerate(nums)}
    for index, num in enumerate(nums):
        result = position.get(target - num)
        if result and result != index:
            return index, result


if __name__ == "__main__":
    test = [1, 3, 9, 7]
    target = 12
    index, result = two_sum(test, target)
    print(index, result)
