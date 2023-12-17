from typing import List


def main(nums: List[int]) -> List[List[int]]:
    """全排列问题

    使用回溯算法处理

    Args:
        nums (List[int]): 原数组

    Returns:
        List[List[int]]: 原数所有可能的排列
    """
    ans: List[List[int]] = []
    size = len(nums)
    if not size:
        return ans

    back_track(nums, size, ans)

    return ans


def back_track(
    nums: List[int],
    size: int,
    ans: List[List[int]],
    start_at: int = 0,
):
    """回溯处理函数

    Args:
        nums (List[int]): 原数组
        size (int): 原数组长度
        ans (List[List[int]]): 结果
        first (int, optional): 开始的位置. Defaults to 0.
    """
    # * 当遍历到数组边界，也就是数字填写完成，就停止回溯
    if start_at == size:
        ans.append(nums[:])

        return

    # * 对数组的每个位置进行填充，每填充一次，下个位置的数字继续进入回溯
    for i in range(start_at, size):
        # * 使用交换的方式填数字
        nums[start_at], nums[i] = nums[i], nums[start_at]

        # * 填完当前数字，继续填下一个数字
        back_track(nums, size, ans, start_at + 1)

        # * 由于使用的是原始的数组，需要将交换更改回撤
        nums[i], nums[start_at] = nums[start_at], nums[i]


if __name__ == "__main__":
    input_arr = [1, 2, 3, 4]
    print(main(input_arr))
