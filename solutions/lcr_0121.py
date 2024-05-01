from typing import List


def main(plants: List[List[int]], target: int) -> bool:
    """二维数组搜索，转BST法

    Args:
        - plants (List[List[int]]): 二维数组
        - target (int): 目标值

    Returns:
        - bool: 搜索结果
    """
    if not plants:
        return False

    x_size = len(plants[0])
    y_size = len(plants)

    x, y = 0, y_size - 1

    # * 从右上角向左下角看，可以看成一颗二叉搜索树
    # 左上角元素的左边（BST左子树）的元素比自身小，
    # 左上角元素的下边（BST右子树）的元素比自身大
    while y >= 0 and x < x_size:
        # * 从左下方往右上方找
        curr = plants[y][x]

        # * 如果当前值比目标值大，沿着 y 方向向上（从BST角度来看是往左）
        if curr > target:
            y -= 1

        # * 当前值比目标值小，沿着 x 方向向右（从BST角度看为往右）
        elif curr < target:
            x += 1
        else:
            return True

    return False


if __name__ == "__main__":
    test_nums = [[2, 3, 6, 8], [4, 5, 8, 9], [5, 9, 10, 12]]
    main(test_nums, 8)
