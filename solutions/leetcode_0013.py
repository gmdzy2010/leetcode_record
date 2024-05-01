def main(s: str) -> int:
    """罗马数字转整数

    Args:
        - s (str): 罗马数字字符串

    Returns:
        - int: 整数
    """
    # * 先建立好罗马数字到阿拉伯数字的映射
    val_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    ans = 0
    size = len(s)
    for i, c in enumerate(s):
        val = val_map[c]
        # * 如果当前位置值比下一位值小，就减掉这个值
        if i < size - 1 and val < val_map[s[i + 1]]:
            ans -= val

        # * 否则就累加
        else:
            ans += val

    return ans


if __name__ == "__main__":
    test_str = "MCMXCIV"
    print(main(test_str))
