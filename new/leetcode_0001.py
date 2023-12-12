from typing import List


def main(nums: List[int], target: int) -> List[int]:
    """求两数之和

    Args:
        nums (List[int]): 原数组
        target (int): 两数之和的目标值

    Returns:
        List[int]: 符合条件的两个数下标
    """
    size = len(nums)
    record = {}

    for i in range(size):
        value = target - nums[i]
        if value in record:
            return [i, record[value]]

        record[nums[i]] = i
    return []


if __name__ == "__main__":
    input_nums = [2, 7, 11, 15]
    print(main(input_nums, 9))
