def three_number_sum_hash(nums):
    index_1, length, result = 0, len(nums), []
    nums.sort()
    # position = {}
    while index_1 < length:
        if nums[index_1] > 0:
            index_1 += 1
            continue
        elif index_1 > 0 and nums[index_1] == nums[index_1 - 1]:
            index_1 += 1
            continue
        
        # use dict to record position.
        index_2 = index_1 + 1
        position = {}
        while index_2 < length:
            if index_2 > index_1 + 2 \
                    and nums[index_2] == nums[index_2 - 1] \
                    and nums[index_2 - 1] == nums[index_2 - 2]:
                continue
            third_num = - (nums[index_1] + nums[index_2])
            if third_num not in position:
                result.append(sorted([nums[index_1], nums[index_2], third_num]))
            else:
                position[third_num] = - (nums[index_1] + nums[index_2])
            index_2 += 1
        index_1 += 1
    return result


def three_number_sum_double_pointer(sequence):
    length, result = len(sequence), []
    sequence.sort()
    for index_1 in range(length):
        if index_1 > 0 and sequence[index_1] == sequence[index_1 - 1]:
            continue
        index_3 = length - 1
        target = -sequence[index_1]
        for index_2 in range(index_1 + 1, length):
            if index_2 > index_1 + 1 and sequence[index_2] == sequence[index_2 - 1]:
                continue
            while index_2 < index_3 and sequence[index_2] + sequence[index_3] > target:
                index_3 -= 1
            if index_2 == index_3:
                break
            if sequence[index_2] + sequence[index_3] == target:
                result.append([sequence[index_1], sequence[index_2], sequence[index_3]])
    return result


if __name__ == '__main__':
    test_sequence = [-1, 0, 1, 2, -1, -4]
    test_result = three_number_sum_hash(test_sequence)
    print(test_result)
