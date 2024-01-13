def main(n: int) -> int:
    """单调递增数字

    Args:
        - n (int): 数字n

    Returns:
        - int: 比n小的最大单调递增数字
    """
    digits = list(str(n))
    size = len(digits)
    if size == 1:
        return n

    # * 倒着遍历每一位（从数字的低位到高位）
    i = size - 1

    # * 注意边界
    while i > 0:
        # * 如果高位比当前位数字大，不满足题意，低位变为9，高位减一
        if digits[i - 1] > digits[i]:
            digits[i:] = ["9"] * (size - i)
            digits[i - 1] = str(int(digits[i - 1]) - 1)

        i -= 1

    # * 将结果转化成数字
    ans = 0
    for d in digits:
        ans = ans * 10 + int(d)

    return ans


if __name__ == "__main__":
    test_n = 332
    print(main(test_n))
