from typing import List, Tuple


def main(s: str):
    """字符串解码

    Args:
        s (str): _description_
    """
    ans = decode_string_stack(s)
    print(ans)

    ans = decode_string_recur(s)
    print(ans)


def decode_string_stack(s: str) -> str:
    """字符串解码，栈版本

    Args:
        - s (str): 原字符串

    Returns:
        - str: 解码之后的字符串
    """
    # * 这里的 ans 作用除了是结果，还是中间处理括号内字符串时的临时变量
    ans = ""

    # * 栈中存放一个两个值的元组
    # * 1.当前层的倍数
    # * 2.当前层的倍数+左括号之前的部分字符串
    # ? 那么，什么是 “当前层倍数+左括号之前的部分字符串”？
    # ! 比如 abc2[def3[gh]mm]nv，指的是 abc 或者 def
    stack: List[Tuple[int, str]] = []

    # * 当前层方括号里面的字符串重复次数，即当前层倍数
    multiple = 0
    for c in s:
        # * 获取倍数，直接使用ASCII范围限制即可
        # ! 倍数有可能不止一位数字，且倍数数字字符串相邻
        if "0" <= c <= "9":
            multiple = multiple * 10 + int(c)

        # * 遇到左括号开始用栈记录倍数和当前已经解码过的字符串结果
        elif c == "[":
            stack.append((multiple, ans))

            # * 当遇到左括号，需要将 ans 先置空，从这里开始记录括号内的字符串
            # ? 为什么这里要将“结果”置空呢？
            # ! 实际上这里的 ans 属于变量复用
            # ! 1.已经解码完成的部分 ans 已经存在栈里面了，将其清空不会丢掉已处理的信息
            # ! 2.置空后的 ans 可以用来记录括号内需要翻倍的字符串
            ans = ""

            # ! multiple 也要立刻归零，防止括号内再次出现倍数需要记录
            multiple = 0

        # * 碰到右括号开始结算本次字符串翻倍操作
        elif c == "]":
            curr_multiple, curr_handled = stack.pop()
            ans = curr_handled + curr_multiple * ans

        else:
            ans += c

    return ans


def decode_string_recur(s: str) -> str:
    """字符串解码，递归版本

    Args:
        - s (str): 原字符串

    Returns:
        - str: 解码之后的字符串
    """
    _, ans = dfs(s, 0)

    return ans


def dfs(s: str, i: int) -> Tuple[int, str]:
    """字符串解码递归函数

    Args:
        s (str): 原字符串
        i (int): 当前字符位置

    Returns:
        Tuple[int, str]: 已经解码的字符串和当前解码到的位置
    """
    ans, multiple = "", 0
    while i < len(s):
        # * 处理倍数
        if "0" <= s[i] <= "9":
            multiple = multiple * 10 + int(s[i])

        # * 遇到左括号开始将后续的字符串递归
        elif s[i] == "[":
            # ! 注意，返回 i 更新了位置
            i, str_already_decoded = dfs(s, i + 1)
            ans += multiple * str_already_decoded
            multiple = 0

        # * 遇到右括号到达递归边界，结束递归，返回新i和处理好的内层解码结果 ans
        elif s[i] == "]":
            return i, ans

        # * 遇到其他，则当字母串处理
        else:
            ans += s[i]

        i += 1

    return i, ans


if __name__ == "__main__":
    test_str = "onm2[abc3[bt]]2[ks]uv"
    main(test_str)
