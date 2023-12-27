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


def get_kth_smallest_of_bst(root: TreeNode | None, k: int) -> int | None:
    """获取BST第k个最小，中序遍历

    看到BST就应该条件反射想到中序遍历

    Args:
        - root (TreeNode | None): 根节点
        - k (int): 待寻找数值

    Returns:
        - int | None: 距离为k的节点值
    """

    stack: List[TreeNode] = []
    while stack or root:
        # * 左边界不断入栈，当到达左边界叶子节点时停止入栈
        while root:
            stack.append(root)
            root = root.left

        # * 节点不断出栈处理
        root = stack.pop()

        # * 每出栈一次，说明距离k缩小一步
        k -= 1

        # * k值减为零时，返回
        if k == 0:
            return root.val

        # * 没有到达k，就继续
        root = root.right

    return None


if __name__ == "__main__":
    test_root = TreeNode(5)
    test_root.left = TreeNode(3)
    test_root.left.left = TreeNode(2)
    test_root.left.left.left = TreeNode(1)
    test_root.left.right = TreeNode(4)
    test_root.right = TreeNode(6)
    print(get_kth_smallest_of_bst(test_root, 3))
