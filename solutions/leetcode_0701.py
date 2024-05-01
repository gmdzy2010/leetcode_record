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


def insert_into_bst(root: TreeNode | None, val: int) -> TreeNode | None:
    """BST插入节点

    Args:
        root (TreeNode | None): 根节点
        val (int): 待插入值

    Returns:
        TreeNode | None: 完成插入的根节点
    """
    new_node = TreeNode(val)

    # * 根节点为空，直接新建
    if not root:
        return new_node

    # * 从根节点开始遍历
    curr = root
    while curr:
        # * 如果 val 比当前节点值小，说明应该去当前节点的左节点
        if val < curr.val:
            # * 左节点为空，新节点作为左节点，完成插入，跳出循环
            if not curr.left:
                curr.left = new_node
                break

            # * 左节点不为空，继续向下找
            curr = curr.left
        else:
            if not curr.right:
                curr.right = new_node
                break
            curr = curr.right

    return root


if __name__ == "__main__":
    test_root = TreeNode(4)

    test_root.left = TreeNode(2)
    test_root.left.left = TreeNode(1)
    test_root.left.right = TreeNode(3)

    test_root.right = TreeNode(7)
    insert_into_bst(test_root, 5)
