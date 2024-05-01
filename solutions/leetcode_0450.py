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


def delete_from_bst_recur(root: TreeNode | None, key: int) -> TreeNode | None:
    """BST删除节点

    Args:
        - root (TreeNode | None): 根节点
        - key (int): 待删除节点的值

    Returns:
        - TreeNode | None: 删除后的根节点
    """
    if not root:
        return None

    # * key 比 当前节点值小，key 有可能在左子树，当前节点的左子树递归删除实现更新
    if key < root.val:
        root.left = delete_from_bst_recur(root.left, key)

    # * key 比 当前节点值大，key 有可能在右子树，当前节点的右子树递归删除实现更新
    elif key > root.val:
        root.right = delete_from_bst_recur(root.right, key)

    # * key 的节点找到了，但左右节点不全，哪个存在就用哪个孩子代替自己作为新的根节点
    elif not root.left or not root.right:
        root = root.left if root.left else root.right

    # * key 的节点找到了，且此节点左右双全
    else:
        # * 取右节点作为后继节点（因为此节点是比 root 值大的最小的节点），取代待删除节点
        successor = root.right

        # * 左右双全一定要走到右子树的最左边
        while successor.left:
            successor = successor.left

        # * 在 root 左子树递归删除后继节点自身（因为自身已经作为被删除的节点替身顶上去了）
        # 原先的右子树删除自己后剩余的右子树再作为取代者 successor 的新的右子树
        # ! 注意这里最好递归删除
        successor.right = delete_from_bst_recur(root.right, successor.val)

        # * 将原先的左子树当成现在的左子树
        successor.left = root.left

        return successor

    return root


if __name__ == "__main__":
    test_root = TreeNode(6)

    test_root.left = TreeNode(1)
    test_root.left.left = TreeNode(0)
    test_root.left.right = TreeNode(3)
    test_root.left.right.left = TreeNode(2)
    test_root.left.right.right = TreeNode(5)
    test_root.left.right.right.left = TreeNode(4)

    test_root.right = TreeNode(8)
    test_root.right.left = TreeNode(7)
    test_root.right.right = TreeNode(9)

    delete_from_bst_recur(test_root, 3)
