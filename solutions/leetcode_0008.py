def main(s: str) -> int:
    """字符串转整数

    注意越界逻辑处理，Python 的大整数相加算法导致整数溢出的边界比较大（理论上不会溢出）

    Args:
        - s (str): 字符串

    Returns:
        - int: 转换出来的整数
    """
    # * 除掉首尾空格
    s = s.strip()
    if not s:
        return 0

    ans = 0

    # * 按照要求整数的范围需要做限制
    int_min, int_max = -(2**31), 2**31 - 1

    # * 大整数边界
    # ! 因为处理连续的数字中间有 * 10 的逻辑，要判断是否越界
    boundary = int_max // 10

    # * 数字符号，可取 +1/-1，取决于 s[0]
    sign = -1 if s[0] == "-" else 1

    # * 遍历开始位置，取决于 s[0]，若没有符号，从 0 开始
    i = 1 if s[0] in ("-", "+") else 0

    for c in s[i:]:
        # * 非数字字符串字节跳出转换
        if not "0" <= c <= "9":
            break

        # * 越界的两种情况：
        # * 结果直接超过边界
        # * 2. 结果没超过边界，但是转换后超过了
        if ans > boundary or ans == boundary and c > "7":
            return int_max if sign == 1 else int_min

        # ans = ans * 10 + ord(c) - ord("0")
        ans = ans * 10 + int(c)

    return ans * sign


if __name__ == "__main__":
    test_str = " -42"
    print(main(test_str))
