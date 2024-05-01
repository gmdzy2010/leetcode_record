from typing import List


def main(nums: List[int]) -> int:
    """连续子数组的最大和

    动态规划求解

    设 i 为数组 nums 某个位置，求最大子数组和 -> 求解以 nums[i] 结尾的最大子数组和
    - 状态数组 dp，其中 dp[i] -> 以 nums[i] 结尾的连续子数组的最大和
    - dp[i] 表示以 nums[i] 结尾的连续子数组的最大和，所以 nums[i] 是一定要加的
    - 若 nums[i] > 0，状态转移方程 dp[i] = dp[i - 1] + nums[i]
        - dp[i - 1] > 0，可以把 nums[i] 接在 dp[i - 1] 代表的数组的后面得到更大和
        - dp[i - 1] <= 0，此时累加 dp[i - 1] 将减小结果，直接取 nums[i] 作为最大和

    - 若 nums[i] < 0，则此次结果也会计算，但最终结果是求 dp 的最大值，最终 nums[i] 参
      与的并且小于零的连续子数组和就会被舍弃掉

    Args:
        - nums (List[int]): 原数组

    Returns:
        - int: 连续子数组的最大和
    """
    size = len(nums)
    if size == 0:
        return 0

    # * 初始化状态数组
    dp = [0 for _ in range(size)]

    # * 使用状态转移方程对 i 和 i-1 进行分析
    for i in range(size):
        if i > 0 and dp[i - 1] > 0:
            dp[i] = dp[i - 1] + nums[i]
        else:
            dp[i] = nums[i]

    return max(dp)


if __name__ == "__main__":
    input_arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(main(input_arr))
