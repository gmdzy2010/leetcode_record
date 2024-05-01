from typing import Self


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


def main(root: TreeNode | None) -> bool:
    """判断二叉树是否平衡

    Args:
        - root (TreeNode | None): 根节点

    Returns:
        - bool: 结果
    """
    res = get_height(root)

    return res != -1


def get_height(node: TreeNode | None) -> int:
    """求二叉树的高度

    二叉树高度
    - 从当前节点到叶子节点的节点数量

    Args:
        - node (TreeNode | None): 当前节点

    Returns:
        - int: 二叉树的当前高度，如果左右子树的高度差大于1（不平衡），则返回 -1
    """
    if not node:
        return 0

    L_height, R_height = get_height(node.left), get_height(node.right)

    # * 如果左右子树不平衡，或者高度差大于1，那么整棵树不平衡
    if L_height == -1 or R_height == -1 or abs(L_height - R_height) > 1:
        return -1

    return 1 + max(L_height, R_height)


if __name__ == "__main__":
    test_root = TreeNode(1)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(2)
    test_root.left.left = TreeNode(3)
    test_root.left.right = TreeNode(4)
    test_root.left.left.left = TreeNode(5)
    print(main(test_root))
