from collections import deque
from typing import Deque, List


def main(s: str):
    """基本计算器
    - 递归方法
    - 逆波兰表达式方法（个人认为更有价值，待理解）

    Args:
        - s (str): 表达式

    Returns:
        - int: 计算结果
    """
    ans1 = calculate_recur(deque(s))
    print(ans1)

    so = Solution()
    ans2 = so.calculate_rpn(s)
    print(ans2)


def calculate_recur(s: Deque[str]) -> int:
    """递归求值函数

    Args:
        - s (Deque[str]): 转成队列的表达式

    Returns:
        - int: 计算结果
    """
    # * 栈中存放当前结算过的结果
    stack: List[int] = []
    sign = "+"

    num = 0
    while len(s) > 0:
        # * 从队列左侧依次出队，
        c = s.popleft()

        # * 处理一位或者连续多位数字字符串
        if c.isdigit():
            num = num * 10 + int(c)

        # * 遇到左括号开始递归计算
        if c == "(":
            num = calculate_recur(s)

        if (not c.isdigit() and c != " ") or len(s) == 0:
            if sign == "+":
                stack.append(num)
            if sign == "-":
                stack.append(-num)
            if sign == "*":
                stack[-1] = stack[-1] * num
            if sign == "/":
                stack[-1] = int(stack[-1] / float(num))

            num = 0
            sign = c

        # * 遇到右括号停止递归，开始清算结果
        if c == ")":
            break

    return sum(stack)


class Solution:
    """计算器，学习别人的解法"""

    def calculate_rpn(self, s: str) -> int:
        """表达式求值

        将常规表达式转成逆波兰表达式，然后使用一个栈求值

        Args:
            - s (str): 表达式字符串

        Returns:
            - int: 计算结果
        """
        return self.eval_from_rpn_tokens(self.get_rpn_tokens(s))

    def get_rpn_tokens(self, s: str) -> List[str]:
        """从常规表达式字符串得到 RPN tokens

        Args:
            - s (str): 表达式字符串

        Returns:
            - List[str]: RPN tokens
        """
        rpn_tokens: List[str] = []

        s += "#"  # endding
        op_priority = {
            "*": 2,
            "/": 2,
            "+": 1,
            "-": 1,
            ")": -1,
            "(": -2,
            "#": -3,
            "$": -4,
        }
        op_stack = ["$"]
        i, n = 0, len(s)
        while i < n:
            # * 处理所有运算符
            if s[i] in op_priority:
                # * 当前运算符为
                # 1. 左括号
                # 2. 比栈顶操作符优先级更高的运算符
                # * 就入栈
                if (
                    s[i] == "("
                    or op_priority[s[i]] > op_priority[op_stack[-1]] > 0
                ):
                    op_stack.append(s[i])

                # 3.当前运算符为右括号，则一直出栈直至栈顶为左括号
                else:
                    # * 如果当前运算符优先级比栈顶的低，就一直出栈并记录在 rpn_tokens
                    while op_priority[s[i]] <= op_priority[op_stack[-1]]:
                        rpn_tokens.append(op_stack.pop())

                    # * 此前已将左右括号之间的运算符 token 全部记录在 rpn_tokens
                    # 将右括号舍弃
                    if s[i] == ")":
                        op_stack.pop()

                    # * 否则将当前运算符入栈
                    else:
                        op_stack.append(s[i])
                i += 1

            # * 处理一位或者连续多位数字字符串 token
            else:
                j = i
                while j < n and s[j].isdigit():
                    j += 1

                rpn_tokens.append(s[i:j])
                i = j

        return rpn_tokens

    def eval_from_rpn_tokens(self, tokens: List[str]) -> int:
        """根据 RPN tokens 计算表达式结果

        Args:
            - tokens (List[str]): RPN tokens

        Returns:
            - int: 计算结果
        """
        stack: List[int] = []
        for token in tokens:
            if token.lstrip("-").isnumeric():
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(self.calculate(num1, num2, token))

        return stack[0]

    def calculate(self, num1: int, num2: int, operator: str) -> int:
        """计算二元表达式结果

        Args:
            - num1 (int): 数值1
            - num2 (int): 数值2
            - operator (str): 运算符

        Returns:
            - int: 计算结果
        """
        if operator == "+":
            return num1 + num2
        if operator == "-":
            return num1 - num2
        if operator == "*":
            return num1 * num2
        return int(num1 / num2)


if __name__ == "__main__":
    test_str = "2*(5+5*2)/3+(16/2+8)"
    main(test_str)
