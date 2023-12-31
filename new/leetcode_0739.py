from typing import List


def main(temperatures: List[int]) -> List[int]:
    """每日温度，单调栈法

    Args:
        temperatures (List[int]): 温度列表

    Returns:
        List[int]: 升温的天数列表
    """
    size = len(temperatures)
    ans = [0] * size

    # * 栈中存放的是位置，且从栈底到栈顶单调递增
    stack: List[int] = []
    for i, t in enumerate(temperatures):
        # * 如果当前温度比栈顶温度高，说明比栈顶的那天温度高的最近的一天找到了
        while stack and t > temperatures[stack[-1]]:
            last_lower_i = stack.pop()
            ans[last_lower_i] = i - last_lower_i

        stack.append(i)

    return ans
