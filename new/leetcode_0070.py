def main(n: int) -> int:
    """爬楼梯

    Args:
        - n (int): 数字

    Returns:
        - int: 总共的方案
    """
    if n < 2:
        return n

    # * dp[i] 代表跳跃 n 个台阶的方案数量
    # ! 因为 0 没有意义，所以 dp 数组多一个元素
    dp = [0] * (n + 1)

    # * 初始化没有dp[0]，其没有意义
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[n]


def main_1(n: int) -> int:
    """爬楼梯，滚动数组

    Args:
        - n (int): 数字

    Returns:
        - int: 总共的方案
    """
    if n < 2:
        return n

    # * 滚动初始化
    dp_1, dp_2 = 1, 2

    for _ in range(3, n + 1):
        dp_i = dp_1 + dp_2

        # * 下一轮计算的 dp_1, dp_2 引用本轮的 dp_2, dp_i
        dp_1, dp_2 = dp_2, dp_i

    return dp_2


def main_2(n: int) -> int:
    """爬特定楼梯

    扩展：7的倍数台阶不能跳

    Args:
        - n (int): 数字

    Returns:
        - int: 总共的方案
    """
    if n < 2:
        return n

    # * dp[i] 代表跳跃 n 个台阶的方案数量
    # ! 因为 0 没有意义，所以 dp 数组多一个元素
    dp = [0] * (n + 1)

    # * 初始化没有dp[0]，其没有意义
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1] if i % 7 != 0 else 0

    return dp[n]


def main_3(n: int) -> int:
    """爬楼梯，矩阵快速幂

    Args:
        - n (int): 数字

    Returns:
        - int: 总共的方案
    """
    if n < 2:
        return n

    return n


if __name__ == "__main__":
    print(main(7))
