from typing import List


def is_valid(s: str) -> bool:
    """有效的括号

    存在三种情况：
    - 左括号多余了
    - 右括号多余了
    - 左右括号数量相同，但不匹配

    Args:
        s (str): 字符串

    Returns:
        bool: 结果
    """
    stack: List[str] = []
    for c in s:
        if c == "(":
            stack.append(")")
        elif c == "{":
            stack.append("}")
        elif c == "[":
            stack.append("]")

        # * 如果遍历过程中栈就空了，说明一定出现了右括号没找到左括号的情况
        elif not stack:
            return False

        # * 如果括号都匹配，那么栈顶元素一定和当前元素相等
        elif stack[-1] != c:
            return False
        else:
            stack.pop()

    return not stack


if __name__ == "__main__":
    test_s = "((([]{})))]"
    is_valid(test_s)
