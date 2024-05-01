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


def is_complete_tree(root: TreeNode | None) -> bool:
    """判断完全二叉树

    使用二叉树层序遍历模版(BFS)
    - 记录每一个节点的对应的满二叉树位置
    - 比较最后一个节点的位置是否和节点数量相等

    Args:
        - root (TreeNode | None): 二叉树根节点

    Returns:
        - bool: 是否完全二叉树
    """
    # * 使用一个元组列表记录经过的节点和对应的位置索引
    nodes: List[Tuple[TreeNode | None, int]] = []
    nodes.append((root, 1))

    i = 0
    # ! 注意这里的 len(nodes) 不能预计算，因为循环过程中长度会发生变化
    while i < len(nodes):
        node, index = nodes[i]

        # * 不管左右节点是否为空，都将其对应的满二叉树位置索引记录下来
        if node:
            nodes.append((node.left, 2 * index))
            nodes.append((node.right, 2 * index + 1))

        i += 1

    # * 只需要判断最后一个节点的位置索引是否和该二叉树的数量是否一样即可
    ans = nodes[-1][1] == len(nodes)

    return ans


if __name__ == "__main__":
    test_root_1 = TreeNode(1)

    test_root_1.left = TreeNode(2)
    test_root_1.left.left = TreeNode(4)
    test_root_1.left.right = TreeNode(5)

    test_root_1.right = TreeNode(3)
    test_root_1.right.left = TreeNode(6)

    print(is_complete_tree(test_root_1))
