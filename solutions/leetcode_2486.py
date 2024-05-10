def main(s: str, t: str) -> int:
    """追加字符以获得子序列，双指针

    Args:
        - s (str): 字符串s
        - t (str): 字符串t

    Returns:
        - int: 在 s 追加的最少字符串数量
    """
    i, j, size_s, size_t = 0, 0, len(s), len(t)

    # * 在字符串t遍历
    while j < size_t:
        # * 只要 i/j 字符不相等，就跳过 i 位置
        while i < size_s and s[i] != t[j]:
            i += 1

        # * 如果i到了 s 末尾，说明 t 剩余的部分都需要追加在 s 后面
        if i == size_s:
            return size_t - j

        i += 1
        j += 1

    return 0


if __name__ == "__main__":
    print(main("coaching", "coding"))
