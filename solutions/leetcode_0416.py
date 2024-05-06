from typing import List


def main(nums: List[int]):
    """分割等和子数组，DP背包

    Args:
        - nums (List[int]): 原数组
    """
    ans1 = can_partition_dp_1D(nums)
    print(ans1)

    ans2 = can_partition_dp_2D(nums)
    print(ans2)


def can_partition_dp_1D(nums: List[int]) -> bool:
    """分割等和子数组，DP背包一维

    Args:
        - nums (List[int]): 原数组

    Returns:
        - bool: 数组是否可以拆分成等和的两部分
    """
    target = sum(nums)
    if target % 2 == 1:
        return False

    # * 先得到拆分成两部分的目标和
    target = target // 2

    # * dp[i] 代表容量是 i 的背包可以凑出来的最大和
    dp = [0] * (target + 1)

    for num in nums:
        # ! 倒着遍历可以防止物品（nums中的数字）重复选取
        for i in reversed(range(num, target + 1)):
            dp[i] = max(dp[i], dp[i - num] + num)

    return target == dp[target]


def can_partition_dp_2D(nums: List[int]) -> bool:
    """分割等和子数组，DP背包二维

    Args:
        - nums (List[int]): 原数组

    Returns:
        - bool: 数组是否可以拆分成等和的两部分
    """
    target = sum(nums)
    nums = sorted(nums)

    # * 如果数组求和的一半不是 0，说明无论如何不可能分成两部分和相等的数组
    if target % 2 != 0:
        return False

    # * 先得到拆分成两部分的目标和，当成背包最大容量
    target = target // 2

    row, col = len(nums), target + 1

    # * dp[i][j] 代表从 nums 0~i 选任意多个，凑出来和为 j
    dp = [[0 for _ in range(col)] for _ in range(row)]

    # * 初始化
    for i in range(row):
        dp[i][0] = 0

    for j in range(1, target):
        # * 如果和比首个数字大，将第一行选择的数字都设置成第一个数字
        if j >= nums[0]:
            dp[0][j] = nums[0]

    # ! 先遍历物品再遍历背包
    for i in range(1, row):
        # * 此问题中，每个数字就代表自身的重量和价值
        i_weight = nums[i]
        i_value = nums[i]

        for j in range(1, col):
            # * 如果当前的累加和已经比当前元素小，说明本次不能累加当前的价值
            if j < i_weight:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - i_weight] + i_value)

    return target == dp[-1][col - 1]


if __name__ == "__main__":
    test_nums = [1, 2, 3, 5]
    main(test_nums)
