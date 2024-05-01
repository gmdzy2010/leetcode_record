from typing import Dict, Self, Set


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


def main(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode | None:
    """最近公共祖先

    - 使用哈希表记录整棵树的子->父的映射关系
    - 使用集合记录从其中一个节点一直往上找的所有节点
    - 从另一个节点开始一直往上找，直到找到在集合中的节点，即为最近公共祖先节点

    Args:
        - root (TreeNode): 树的根节点
        - p (TreeNode): 树中的某个节点
        - q (TreeNode): 树中的另外一个节点

    Returns:
        - TreeNode | None: p和q的最近公共祖先节点
    """
    # * 使用哈希表记录所有子到父节点的映射关系
    ancestors: Dict[TreeNode | None, TreeNode | None] = {}

    # * 根节点的父节点是自己
    ancestors[root] = root

    # * 构建整个子->父的映射关系
    process(root, ancestors)

    # * 用集合记录 p 节点往上找的所有祖先
    visited: Set[TreeNode | None] = set()

    # * 将根节点单独放入
    visited.add(root)

    # * 从 p 节点往上找，那么所有经过的节点就在 p_visited 这个集合
    curr = p
    while curr != ancestors.get(curr):
        visited.add(curr)
        curr = ancestors.get(curr)

    # * 从 q 节点往上找，如果不在集合 p_visited 里面的就一直往上，直到在集合里面
    curr = q
    while curr not in visited:
        curr = ancestors.get(curr)

    return curr


def process(
    root: TreeNode | None,
    ancestors: Dict[TreeNode | None, TreeNode | None],
):
    """构造父子关系映射哈希表

    递归遍历

    Args:
        - root (TreeNode | None): 根节点
        - ancestors (Dict[TreeNode | None, TreeNode | None]): 父子节点关系
    """
    if not root:
        return

    ancestors[root.left] = root
    ancestors[root.right] = root
    process(root.left, ancestors)
    process(root.right, ancestors)


if __name__ == "__main__":
    test_root = TreeNode(3)

    test_root.left = TreeNode(5)
    test_root.right = TreeNode(1)

    test_root.left.left = TreeNode(6)
    test_root.left.right = TreeNode(2)
    test_root.right.left = TreeNode(0)
    test_root.right.right = TreeNode(8)

    test_root.left.right.left = TreeNode(7)
    test_root.left.right.right = TreeNode(4)
