from typing import List


def main(strs: List[str], m: int, n: int) -> int:
    """一和零，DP-01背包

    Args:
        - strs (List[str]): 原数字字符串列表
        - m (int): 最终的集合包含的 0 数量
        - n (int): 最终的集合包含的 1 数量

    Returns:
        - int: 满足 m/n 限制的元素最多子集合元素数量
    """
    # * dp[i][j] 代表最多有 i 个 0 和 j 个 1 的最大子集合元素数量
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for s in strs:
        # * 分别统计每个数字字符串的 0 和 1 的数量
        cnt_zero, cnt_one = 0, 0
        for c in s:
            if c == "0":
                cnt_zero += 1
            else:
                cnt_one += 1

        # * 01背包问题的一维解法需要倒叙遍历
        for i in range(m, cnt_zero - 1, -1):
            for j in range(n, cnt_one - 1, -1):
                # ! 对于每个物品 s，不要它意味着需要去掉 s 中的所有 0 和 1
                dp[i][j] = max(dp[i][j], dp[i - cnt_zero][j - cnt_one] + 1)

    return dp[-1][-1]


if __name__ == "__main__":
    test_strs = ["10", "0001", "111001", "1", "0"]
    print(main(test_strs, 5, 3))
