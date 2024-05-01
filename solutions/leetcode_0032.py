from typing import List


def main(s: str):
    """最长有效括号
    - 栈
    - 动态规划

    Args:
        - s (str): 原字符串
    """
    ans1 = longest_valid_parentheses_stack(s)
    print(ans1)

    ans2 = longest_valid_parentheses_dp(s)
    print(ans2)


def longest_valid_parentheses_stack(s: str) -> int:
    """最长有效括号，栈方法

    用栈记录无法匹配的括号的索引位置，然后遍历栈，两个无法匹配括号的索引之间的长度就是
    能够匹配括号的字串长度，取最大即可

    Args:
        - s (str): 原字符串

    Returns:
        - int: 最长有效括号长度
    """
    # * 存当前字符的下标
    # ! 栈底始终为当前已经遍历过的元素中"上一个没有被匹配的右括号的下标"
    # ! 栈中两个元素之间的区间肯定是有效的
    stack: List[int] = []

    ans = 0

    for i, c in enumerate(s):
        # * 如果栈非空且当前为右括号，且栈顶对应的字符串是左括号，就出栈
        if stack and c == ")" and s[stack[-1]] == "(":
            stack.pop()

            # * 如果出栈后栈空，说明[0, i]区间有效
            # * 否则 [stack[-1], i]区间有效
            ans = max(ans, i - (stack[-1] if stack else -1))

        # * 如果栈空
        # * 当前字符为左括号（需要找到右括号）
        # * 如果当前字符为右括号，栈顶记录也是右括号（不合格，永远不会被pop出去）
        else:
            stack.append(i)

    return ans


def longest_valid_parentheses_dp(s: str) -> int:
    """最长有效括号，DP

    Args:
        - s (str): 原字符串

    Returns:
        - int: 最长有效括号长度
    """
    size = len(s)
    ans = 0
    if size == 0:
        return ans

    # * dp[i] 代表以 s[i] 结尾的最长有效括号长度
    # ! 注意这里是"以 s[i] 结尾"，并非 s[i] 之前的有效区间都包含
    # 比如 "())"，dp[2] = 0，因为以 s[i] 结尾的是一个右括号，肯定无效
    dp = [0] * size

    for i, c in enumerate(s):
        if i > 0 and c == ")":
            # ! t 是与 i 对称的位置
            # ? 为什么呢？
            # * dp[i - 1] 代表 i 之前连续有效的区间跳过，到达和当前括号对称的位置
            # * 但对称的位置上不一定有效，所以需要判断对称位置上是否是左括号
            t = i - dp[i - 1] - 1

            # * 当上一个字符和当前字符组成有效括号对的时候，dp[i] 由 dp[i-2] 迁移而来
            # "...  (  ) ..."
            # "... i-1 i ..."
            if s[i - 1] == "(":
                dp[i] = dp[i - 2] + 2

            # ! s[i-1] 位置上是右括号其实说明以 s[i-1] 结尾的字符串有一段有效区间
            # * dp[t-1] t 位置之前连续有效的区间长度
            # * dp[i-1] i 位置之前连续有效的区间长度
            # ! t 位置之前的有效区间 + i 之前的有效区间 + i 和 t 位置是一对有效括号
            elif s[i - 1] == ")" and t >= 0 and s[t] == "(":
                dp[i] = dp[t - 1] + dp[i - 1] + 2

    ans = max(dp)

    return ans


if __name__ == "__main__":
    test_str = ")()())((())))()()"
    print(main(test_str))
