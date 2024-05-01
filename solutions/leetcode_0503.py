from typing import List


def main(nums: List[int]) -> List[int]:
    """下一个更大的元素

    使用单调栈，自底向上逐渐递减

    Args:
        - nums (List[int]): 原始数组

    Returns:
        - List[int]: 结果
    """
    size = len(nums)

    # * 初始化结果数组全部为 -1
    ans = [-1] * size

    # * 单调栈保存的是一个单调递减的连续区间，一旦下一个位置是拐点，栈顶的最近最大就找到了
    stack: List[int] = []

    # * 为了能访问到循环后的元素，把数组的下标范围扩大两倍
    for i in range(2 * size - 1):
        # * 比较栈顶下标和 i 位置元素，看看 i 是不是栈顶下标元素的最近最大位置
        while stack and nums[stack[-1]] < nums[i % size]:
            last_i = stack.pop()

            # * last_i 位置的最近最大元素位置为 i，将结果存储即可
            ans[last_i] = nums[i % size]

        # * 避免重复计算，后续的最近最大元素其实是转一圈又回来了
        if i < size:
            stack.append(i)

    return ans


if __name__ == "__main__":
    test_nums = [1, 2, 3, 4, 3, 2, 7]
    print(main(test_nums))
