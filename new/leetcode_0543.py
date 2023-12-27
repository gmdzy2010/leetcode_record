from typing import Self, Tuple


class TreeNode:
    """二叉树节点"""

    def __init__(
        self,
        val: int = 0,
        left: Self | None = None,
        right: Self | None = None,
    ):
        self.val = val
        self.left: Self | None = left
        self.right: Self | None = right

    def __str__(self) -> str:
        return f"{self.val}"

    def __repr__(self) -> str:
        if self.left and self.right:
            return f"{self.left} <- node: {self.val} -> {self.right}"
        if self.left and not self.right:
            return f"{self.left} <- node: {self.val} -> _"
        if not self.left and self.right:
            return f"_ <- node: {self.val} -> {self.right}"
        return f"_ <- node: {self.val} -> _"


def main(root: TreeNode | None):
    """二叉树的最大深度
    - 递归（DFS）
    - 队列

    Args:
        - root (TreeNode | None): 根节点
    """
    diameter, _ = get_diameter(root)
    print(diameter)


def get_diameter(node: TreeNode | None) -> Tuple[int, int]:
    """二叉树的直径，递归版本

    直径：任意两个节点间的最大距离

    Args:
        - node (TreeNode | None): 头节点

    Returns:
        - Tuple[int, int]: 以 node 为根的最大距离和高度
    """
    if not node:
        return 0, 0

    # * 分别计算左右子树的最大距离
    L_max_distance, L_height = get_diameter(node.left)
    R_max_distance, R_height = get_diameter(node.right)

    # * 如果最大距离不经过当前节点，则最大距离是左子树右子树最大距离中的较大值
    max_distance_1 = max(L_max_distance, R_max_distance)

    # ! 叶子节点高度是 1，所以 distance = height - 1
    # * 如果最大距离经过当前节点，最大距离是左右子树最大距离的和再加1（经过当前节点）
    max_distance_2 = (L_height - 1) + 2 + (R_height - 1)

    # * 取经过或者不经过当前节点两种情况的最大值
    max_distance = max(max_distance_1, max_distance_2)

    height = max(L_height, R_height) + 1

    return max_distance, height


if __name__ == "__main__":
    test_root = TreeNode(1)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(2)
    test_root.left.left = TreeNode(3)
    test_root.left.right = TreeNode(4)
    test_root.right.left = TreeNode(4)
    test_root.right.right = TreeNode(3)
    main(test_root)
