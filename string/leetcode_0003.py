from typing import Set


def main(string: str) -> int:
    """无重复字符的最长子串

    解题方法：滑动窗口

    概念约定
    - string：原字符串
    - max_sub_str(i)：获取以 i 处字符开头的无重复字符的最长子串的函数

    解题思路
    假设 max_sub_str(i) 的结束位置为 j，则有
        - string[(i + 1)...j] 上的字符必然不重复
        - string[i] == string[j + 1]
        - 忽略字符顺序：string[i...j] == string[(i + 1)...(j + 1)]

    对于 max_sub_str(i + 1)，没有了第 i 个字符，j + 1 处又和 i 处字符相等，此时有可能获
    得比 string[L...R] 更长的无重复子串。在 string 的每个位置上重复上面的搜索过程即可获得
    结果。

    Args:
        - strings (str): 原字符串

    Returns:
        - int: 无重复字符的最长子串长度
    """
    string_len = len(string)
    if string_len < 2:
        return string_len

    # * 用集合存储当前窗口内的无重复字符
    unique: Set[str] = set()

    # * 当前无重复字符子串最大长度
    max_length = 0

    # * 右指针
    R = 0

    # * 用左指针 L 在整个字符上遍历
    for L in range(string_len):
        # * 移动 R
        # 当 R 处字符不在窗口字符集合中时加入，并继续向右找，到 R 处字符已经在集合中时停止
        # 实际上循环结束的时候，右指针已经到了下一个位置
        while R < string_len and string[R] not in unique:
            unique.add(string[R])
            R += 1

        # * 此时的子串长度即为以L开头的无重复字符子串最大长度
        max_length = max(max_length, R - L)

        # * 如果 L 之后的子串长度已经小于或者等于最大无重复字符子串长度，没必要再找了
        if string_len - L + 1 <= max_length:
            return max_length

        # * 从窗口字符集合中移除 L 处字符
        # 为下一轮寻找以 L + 1 处字符开头的无重复字符子串做准备
        unique.remove(string[L])

    return max_length


if __name__ == "__main__":
    input_str = "aaabcabcdcadb"
    print(main(input_str))
