def main(num1: str, num2: str) -> str:
    """字符串相乘

    Args:
        - num1 (str): 数字字符串1
        - num2 (str): 数字字符串2

    Returns:
        - str: 乘法运算后的数字字符串
    """
    if num1 == "0" or num2 == "0":
        return "0"

    size_1, size_2 = len(num1), len(num2)

    # * 初始化相乘结果，这两个数字相乘结果最多有 size_1 + size_2 位
    res = [0] * (size_1 + size_2)

    # * 从个位数开始计算
    for i in range(size_1 - 1, -1, -1):
        for j in range(size_2 - 1, -1, -1):
            # * 保留两个指针位置
            # ? 为什么指针位置是这个？
            # * 两个一位数字乘法结果最多有两位，低位 p 和高位 q 和下标的对应关系
            p = i + j + 1
            q = i + j

            # * 先计算两个数乘积
            multi = int(num1[i]) * int(num2[j])

            # * 每一轮的乘积累加低位之前的结果
            total = multi + res[p]

            # * 计算进位和余数
            carry, remainder = total // 10, total % 10

            # * 低位更新为余数
            res[p] = remainder

            # * 高位累加进位
            res[q] += carry

    # * 如果最高位为零，就去掉最高位
    if res[0] == 0:
        return "".join(str(c) for c in res[1:])

    return "".join(str(c) for c in res)


if __name__ == "__main__":
    test_str1, test_str2 = "123", "4567"
    main(test_str1, test_str2)
