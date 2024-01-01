from typing import List


def main(s: str) -> str:
    """删除所有相邻重复字符

    Args:
        s (str): 原字符串

    Returns:
        str: 删除后的字符串
    """
    stack: List[str] = []
    for c in s:
        # * 当栈不为空且栈顶和当前字符串相同，就出栈
        if stack and stack[-1] == c:
            stack.pop()

        else:
            stack.append(c)

    return "".join(stack)


if __name__ == "__main__":
    test_str = "abbac"
    main(test_str)
