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
    pass


if __name__ == '__main__':
    test_sequence = [-1, 0, 1, 2, -1, -4]
    test_result = three_number_sum_hash(test_sequence)
    print(test_result)
