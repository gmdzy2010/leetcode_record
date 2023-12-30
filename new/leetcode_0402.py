from typing import List


def remove_k_digits(num: str, k: int) -> str:
    """移除k个数字

    Args:
        num (str): 数字字符串
        k (int): 要移除的位数

    Returns:
        str: 移除完的最小数字
    """
    stack: List[str] = []
    for c in num:
        # * 从单调栈当中移除所有比当前数字大的元素
        while k and stack and stack[-1] > c:
            stack.pop()
            k -= 1

        # * 再将当前数字加入栈，此时栈中数字一定是当前能够构成的最小数字
        stack.append(c)

    # * 如果遍历完栈中一直保持单调递增，字节删除最后的位数字得到的即最小
    stack = stack[:-k] if k else stack

    return "".join(stack).lstrip("0") or "0"
