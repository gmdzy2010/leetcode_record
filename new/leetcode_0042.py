from typing import List


def main(height: List[int]) -> int:
    """接雨水问题

    使用单调栈求解

    对于位置 i，有：
    - 雨水能到达的最大高度等于位置 i 两边的最大高度的最小值
    - 能接的雨水量等于位置 i 处的水能到达的最大高度减去 height[i]

    单调栈维持的是一个柱子高度单调下降的区域，栈顶一直保持的是当前区域的最低洼处，一旦最低洼处
    旁边有了比它更高的柱子，说明可以形成凹槽接水了，此时出栈一个柱子位置相当于用水填平当前的凹
    槽，横向计算即可

    Args:
        height (List[int]): 高度数组

    Returns:
        int: 能接雨水的数量
    """
    ans = 0

    # * 使用单调栈维护访问过的高度元素位置，从栈底到栈顶保持位置单调递减
    stack: List[int] = []

    for i, h in enumerate(height):
        # * 当出现比栈顶元素高的柱子，说明出现了凹槽，可以接水了
        while stack and h > height[stack[-1]]:
            # * 可接水区域的右边界是栈顶
            min_h = stack.pop()

            # * 栈空了说明出现了一个柱子一直升高的区域
            if not stack:
                break

            # * 可接水区域的左边界是凹槽左边的柱子位置，即当前栈顶
            sub_min_h = stack[-1]
            area_w = i - sub_min_h - 1

            # * 高度就是最小的柱子和凹槽处柱子之间的高度差值
            area_h = min(height[sub_min_h], h) - height[min_h]
            ans += area_w * area_h

        # * 计算完可接水区域后的第一个柱子位置入栈
        stack.append(i)

    return ans


if __name__ == "__main__":
    input_arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(main(input_arr))
