def main(n: int):
    """斐波那契数列

    Args:
        n (int): 数字
    """
    ans1 = fib_recur(n)
    print(ans1)


def fib_recur(n: int) -> int:
    """斐波那契数列，递归版
    - 时间复杂度O(2^n)，准确点事O(1.618^n)

    Args:
        - n (int): 斐波那契数举上限

    Returns:
        - int: 斐波那契数列之和
    """
    if n < 2:
        return n

    return fib_recur(n - 1) + fib_recur(n - 2)


def fib_dp(n: int) -> int:
    """斐波那契数列，动态规划版
    - 时间复杂度O(n)

    Args:
        - n (int): 斐波那契数举上限

    Returns:
        - int: 斐波那契数列之和
    """
    if n < 2:
        return n

    # * 初始状态
    p, q, r = 0, 0, 1
    for _ in range(2, n + 1):
        p, q = q, r
        r = p + q

    return r
