from typing import List


def calculate(s: str) -> int:
    """基本计算器，栈方法

    Args:
        s (str): 字符串表达式

    Returns:
        int: 计算结果
    """
    # * 符号栈，存放每一层的符号（每层括号表示一层）
    stack: List[int] = []

    # * 栈顶为当前层的符号，初始为 +1
    stack.append(1)

    # * 当前数字的符号，取 +1 或 -1
    sign = 1

    size = len(s)
    i = 0
    ans = 0
    while i < size:
        # * 处理连续的数字字符串
        if s[i].isdigit():
            num = 0
            while i < size and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1

            # * 考虑符号影响
            ans += sign * num
        else:
            if s[i] == "+":
                sign = stack[-1]

            # * 当遇到 - 运算符，整层的符号都要变化
            elif s[i] == "-":
                sign = -stack[-1]

            # * 遇到左括号，栈顶更新当前层的符号
            elif s[i] == "(":
                stack.append(sign)

            # * 遇到右括号，弹出本层符号
            elif s[i] == ")":
                stack.pop()

            # * 其他情况（如空格等）直接跳过即可
            i += 1

    return ans


if __name__ == "__main__":
    test_str = "(1+(4+5+2)-3)+(6+8)"
    print(calculate(test_str))
