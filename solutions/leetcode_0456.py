from typing import List


def main(nums: List[int]) -> bool:
    """132模式，单调栈方法

    Args:
        - nums (List): 原数组

    Returns:
        - bool: 是否存在132模式
    """
    # * 单调栈中维护的是一个单调递减的一系列 2 （次最大）
    stack: List[int] = []

    # * k 即代表132模式中的 2
    k = float("-inf")

    for num in reversed(nums):
        # * 找符合 132 模式 1 < 2 条件的 1
        if num < k:
            return True

        # * 如果栈顶元素比当前枚举的 num 小，此时：
        # * 把本轮枚举的 num 当成 3，栈顶当成 2，满足了 132 的 3 > 2 ，后续循环找 1 < 2
        # * 一直往外弹出，直到找到——小于 3 的最大 2
        # ? 为什么要执着于找到最大的 2 呢？
        # * 因为 2 不够小，将导致后序针对 1 的枚举错过符合条件的结果
        while stack and stack[-1] < num:
            # * 相当于找到2（132模式的次最大），保存下来，给后面的循环轮次找 1 用
            k = stack.pop()

        stack.append(num)

    return False


if __name__ == "__main__":
    test_nums = [1, 2, 3, 4]
    print(main(test_nums))
