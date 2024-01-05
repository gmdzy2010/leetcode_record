def main(num1: str, num2: str) -> str:
    """字符串相加，二进制加法

    Args:
        - num1 (str): 数字字符串1
        - num2 (str): 数字字符串2

    Returns:
        - str: 加法运算后的数字字符串
    """
    ans = ""

    # * 从最后一位字符串开始，因为要模拟加法运算
    i, j = len(num1) - 1, len(num2) - 1

    # * 加法的进位
    carry = 0

    while i >= 0 or j >= 0:
        # * 先将每一位上的字符串转数字
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0

        # * 将数字和当前的进位数值加起来
        total = n1 + n2 + carry

        # * 再根据加起来的数字计算进位数字和进位之后剩余的当前位数字（余数）
        carry, remainder = total // 2, total % 2

        ans = str(remainder) + ans

        i -= 1
        j -= 1

    # * 如果处理之后进位数不为零，在最前面加1
    ans = ans if carry == 0 else "1" + ans

    return ans


if __name__ == "__main__":
    test_str1, test_str2 = "1101", "110"
    main(test_str1, test_str2)
