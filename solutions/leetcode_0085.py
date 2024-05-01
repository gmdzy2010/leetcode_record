from typing import List


def main(matrix: List[List[str]]) -> int:
    """求矩阵最大矩形面积

    Args:
        - matrix (List[List[str]]): 原字符串矩阵

    Returns:
        - int: 最大矩形面积
    """
    x_size = len(matrix[0])
    y_size = len(matrix)
    heights = [0] * x_size
    ans = 0

    # * 从矩阵构造高度数组，就和84题一样了，在y方向上累加
    for y in range(y_size):
        for x in range(x_size):
            dot = matrix[y][x]

            # * 只要当前位置不是 1，就将之前在 y 方向上累加的高度清空
            heights[x] = heights[x] + 1 if dot == "1" else 0

        # * 对于每一层 heights 数组都有可能变化，都计算一遍最大矩形面积
        ans = max(ans, largestRectangleArea(heights))

    return ans


def largestRectangleArea(heights: List[int]) -> int:
    """根据高度数组求最大面积

    Args:
        - heights (List[int]): 高度数组

    Returns:
        - int: 最大面积
    """
    ans = 0

    # * 原始高度数组加入哨兵节点，
    heights = [0] + heights + [0]
    size = len(heights)

    # * 相应地，记录单调递增的单调栈首先入栈最低的值的位置
    stack: List[int] = [0]

    # * 哨兵数据只是用来减少判断的，需要跳过它
    # ! 可以取到最后一个高度值，因为需要将栈中所有的位置都弹出
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

        stack.append(i)

    return ans


if __name__ == "__main__":
    test_matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    main(test_matrix)
