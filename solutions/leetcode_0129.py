from typing import List, Self, Tuple


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
    """求根到叶值组合之和

    Args:
        - root (TreeNode | None): 根节点
    """
    ans = sum_root_2_leaf_val(root)
    print(ans)


def sum_root_2_leaf_val(root: TreeNode | None) -> int:
    """求根到叶值组合之和

    - 使用二叉树深度优先遍历模版
    - 和求二叉树所有路径一个套路

    Args:
        - node (TreeNode | None): 头节点

    Returns:
        - int: 所有根节点到叶子节点路径经过节点值拼接成的字符串转数字之和
    """
    if not root:
        return 0

    # * 存放所有从根节点到叶子节点路径经过的所有节点值拼接成的数字字符串
    res: List[str] = []

    # * 存放所有节点和该节点的路径数字字符串
    stack: List[Tuple[TreeNode, str]] = []
    stack.append((root, ""))

    while stack:
        node, curr_val_str = stack.pop()
        curr_val_str = curr_val_str + str(node.val)

        # * 仍然是到达叶子节点结算
        if not node.left and not node.right:
            res.append(curr_val_str)

        if node.left:
            stack.append((node.left, curr_val_str))
        if node.right:
            stack.append((node.right, curr_val_str))

    return sum(int(val_str) for val_str in res)


if __name__ == "__main__":
    test_root = TreeNode(1)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(2)
    test_root.left.left = TreeNode(3)
    test_root.left.right = TreeNode(4)
    test_root.right.left = TreeNode(4)
    test_root.right.right = TreeNode(3)
    main(test_root)
