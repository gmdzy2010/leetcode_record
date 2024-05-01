from typing import List, Self


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


def main(root: TreeNode | None) -> TreeNode | None:
    """翻转二叉树

    Args:
        - root (TreeNode | None): 根节点

    Returns:
        - TreeNode | None: 翻转后的根节点
    """
    root1 = invert_tree_recur(root)
    print(root1)

    root2 = invert_tree_stack(root)
    print(root2)

    return root


def invert_tree_recur(root: TreeNode | None) -> TreeNode | None:
    """翻转二叉树

    Args:
        root (TreeNode | None): 根节点

    Returns:
        TreeNode | None: 翻转后的根节点
    """
    if not root:
        return root

    inverted_left = invert_tree_recur(root.left)
    inverted_right = invert_tree_recur(root.right)

    root.left, root.right = inverted_right, inverted_left

    return root


def invert_tree_stack(root: TreeNode | None) -> TreeNode | None:
    """翻转二叉树，非递归版

    Args:
        root (TreeNode | None): 根节点

    Returns:
        TreeNode | None: 翻转后的根节点
    """
    if not root:
        return root

    stack: List[TreeNode] = []
    stack.append(root)
    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

        node.left, node.right = node.right, node.left

    return root


if __name__ == "__main__":
    test_root = TreeNode(1)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(3)
    test_root.left.left = TreeNode(4)
    test_root.left.right = TreeNode(5)
    test_root.right.left = TreeNode(6)
    test_root.right.right = TreeNode(7)
    main(test_root)
