from typing import List


def main(heights: List[int]) -> int:
    """求柱子最大面积，单调栈方法

    单调栈典型应用场景
    - 在一维数组中找第一个满足某种条件的数

    Args:
        - heights (List[int]): 高度数组

    Returns:
        - int: 柱子最大面积
    """
    ans = 0

    # * 原始高度数组加入哨兵节点，
    heights = [0] + heights + [0]
    size = len(heights)

    # * 相应地，记录单调递增的单调栈首先入栈最低的值的位置
    stack: List[int] = [0]

    # * 哨兵数据只是用来减少判断的，需要跳过它
    # ! 可以取到最后一个高度值
    for i in range(1, size):
        # * 1. 在单调栈中，将所有高度比当前高度大的高度弹出
        # * 2. 每弹出一次就计算一次面积最大值
        while heights[i] < heights[stack[-1]]:
            # * 此时栈顶弹出的为 当前位置 i 之前最近的高度最大值
            curr_h = heights[stack.pop()]

            # * 此时的栈顶即离之前高度 curr_h 最近的最大高度值出现的位置
            # 计算面积即可
            curr_w = i - stack[-1] - 1

            ans = max(ans, curr_h * curr_w)

        # ? 这里为什么每个位置都入栈？
        stack.append(i)

    return ans


if __name__ == "__main__":
    test_heights = [2, 1, 5, 6, 2, 3]
    main(test_heights)
