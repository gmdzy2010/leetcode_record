from typing import List


def main(nums: List[int]):
    """打家劫舍

    Args:
        - nums (List[int]): 每个房间的钱数量
    """
    ans1 = rob_1(nums)
    print(ans1)

    ans2 = rob_2(nums)
    print(ans2)


def rob_1(nums: List[int]) -> int:
    """打家劫舍，DP-一维

    Args:
        - nums (List[int]): 每个房间的钱数量

    Returns:
        - int: 能得到的最多的钱
    """
    size = len(nums)

    # * dp[i] 代表前 i 个房子能得到的最大金额
    dp = [0] * (size + 1)

    # * dp[1] 显然是第一个房子的钱
    dp[1] = nums[0]

    for i in range(2, size + 1):
        # * 如果第 i 个房间的钱不要，dp[i] = dp[i-1]
        # * 如果第 i 个房间的钱要，i-1 房间是不能要的，dp[i] = dp[i-2] + nums[i-1]
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

    return dp[-1]


def rob_2(nums: List[int]) -> int:
    """打家劫舍，DP

    Args:
        - nums (List[int]): 每个房间的钱数量

    Returns:
        - int: 能得到的最多的钱
    """
    size = len(nums)
    f = [0] * (size + 2)
    for i, x in enumerate(nums):
        f[i + 2] = max(f[i + 1], f[i] + x)

    # ! 输出抢劫路径
    i = size - 1
    while i >= 0:
        # * 说明 f[i+2] 是从 f[i] 转移来的
        if f[i + 2] == f[i] + nums[i]:
            print(i, nums[i])
            i -= 2

        # * 说明 f[i+2] 是从 f[i+1] 转移来的
        else:
            i -= 1

    return f[-1]


if __name__ == "__main__":
    test_nums = [2, 7, 9, 3, 1]
    print(main(test_nums))
