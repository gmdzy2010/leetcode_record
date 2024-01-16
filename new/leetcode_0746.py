from typing import List


def main(cost: List[int]) -> int:
    """爬楼梯最少花费，动态规划

    这题目叙述是`屎`，鉴定完毕

    从评论找了个说人话的：
    - 花费数组 cost 长度为 n，一共有 n+1 个台阶，编号从 0 到 n
    - 需要从编号为 0 或 1 的台阶开始，向上爬到编号为 n 的台阶，每次只能爬 1 或 2 个台阶
    - 从编号为 i 的台阶向上爬，需要花费 cost[i]
    - 求爬到 n 的花费之和的最小值。

    Example:
        - cost = [10,15,20]，表示有 0, 1, 2, 3 四个台阶，起点为 0 或 1，终点为 3
        - 从编号为 1 的台阶往上爬两个台阶就可以到达终点 3 了，对应花费最小，答案是 15

    Args:
        - cost (List[int]): 花费数组

    Returns:
        - int: 到达编号为 n 的台阶最少花费
    """
    size = len(cost)

    # * dp[i] 代表到达第 i 个台阶需要花费的最少体力值
    dp = [0] * size

    # ? 到达第 0 个台阶为啥也要体力？
    dp[0], dp[1] = cost[0], cost[1]

    # * 到达第 i 个台阶要想花费最少，有两种可能
    # * 1. 到达第 i - 1 个台阶的花费最少
    # * 2. 到达第 i - 2 个台阶的花费最少
    # * 取两者更小，再加上第 i 的体力值
    for i in range(2, size):
        dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]

    # * 最后还有一个台阶，他妈的，都是屎
    return min(dp[size - 1], dp[size - 2])


if __name__ == "__main__":
    test_nums = [10, 15, 20]
    print(main(test_nums))
