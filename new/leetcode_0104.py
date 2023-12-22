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


def main(root: TreeNode | None) -> bool:
    """判断二叉树是否平衡

    Args:
        - root (TreeNode | None): 根节点

    Returns:
        - bool: 结果
    """
    res = get_height(root)

    return True if res != -1 else False


def get_height(node: TreeNode | None) -> int:
    """求二叉树的高度

    二叉树高度
    - 从当前节点到叶子节点的节点数量

    Args:
        node (TreeNode | None): 当前节点

    Returns:
        int: 二叉树的当前高度，如果左右子树的高度差大于1（不平衡），则返回 -1
    """
    if not node:
        return 0

    left_height = get_height(node.left)
    right_height = get_height(node.right)

    # * 如果左右子树不平衡，那么整棵树不平衡
    if left_height == -1:
        return -1
    if right_height == -1:
        return -1

    # * 如果左右子树高度差大于1，也不平衡，若高度差小于等于1返回左右子树的高度
    if abs(left_height - right_height) > 1:
        res = -1
    else:
        res = 1 + max(left_height, right_height)

    return res


if __name__ == "__main__":
    test_root = TreeNode(1)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(2)
    test_root.left.left = TreeNode(3)
    test_root.left.right = TreeNode(4)
    test_root.right.left = TreeNode(4)
    test_root.right.right = TreeNode(3)
    main(test_root)
