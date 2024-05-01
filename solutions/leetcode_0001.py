from typing import List


def main(nums: List[int], target: int) -> List[int]:
    """两数之和

    Args:
        - nums (List[int]): 原数组
        - target (int): 两数之和的目标值

    Returns:
        - List[int]: 符合条件的两个数下标
    """
    size = len(nums)

    # * 用哈希表记录遍历过的元素 -> key，及这个元素在的位置 -> value
    record = {}

    for i in range(size):
        value = target - nums[i]
        # * 目标值已经出现过了，直接从哈希表里面取出来
        if value in record:
            return [i, record[value]]

        # * 不在哈希表里面的元素就记下来这个元素以及位置
        record[nums[i]] = i
    return []


if __name__ == "__main__":
    input_nums = [2, 7, 11, 15]
    print(main(input_nums, 9))
