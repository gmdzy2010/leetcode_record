from typing import Dict, List, Self


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


def find_distance_k_nodes(
    root: TreeNode,
    target: TreeNode,
    k: int,
) -> List[int]:
    """寻找二叉树距离k的节点

    Args:
        - root (TreeNode): 根节点
        - target (TreeNode): 目标节点
        - k (int): 目标距离

    Returns:
        - List[int]: 结果
    """
    parents: Dict[int, TreeNode] = {}
    build_parents_map(root, parents)

    ans: List[int] = []
    find_nodes(parents, ans, target, None, 0, k)

    return ans


def build_parents_map(node: TreeNode, parents: Dict[int, TreeNode]):
    """父节点关系映射关系

    Args:
        - node (TreeNode): 当前节点
        - parents (Dict[int, TreeNode]): 映射关系哈希表
    """
    if node.left:
        parents[node.left.val] = node
        build_parents_map(node.left, parents)
    if node.right:
        parents[node.right.val] = node
        build_parents_map(node.right, parents)


def find_nodes(
    parents: Dict[int, TreeNode],
    ans: List[int],
    node: TreeNode | None,
    prev: TreeNode | None,
    depth: int,
    k: int,
):
    """查找递归函数

    如果当前访问的节点不符合要求，且还没有找过
    - 向下递归查找，深度+1
        - 左节点递归
        - 右节点递归
    - 向上查找，利用父节点映射关系哈希表

    Args:
        - parents (Dict[int, TreeNode]): 节点的父节点关系映射
        - ans (List[int]): 所有距离 target 节点为 k 的节点值
        - node (TreeNode | None): 当前节点
        - prev (TreeNode | None): 上一个节点，用于防止重复遍历
        - depth (int): 深度
        - k (int): 目标距离
    """
    if not node:
        return

    if depth == k:
        ans.append(node.val)
        return

    # * 向下查找
    if node.left != prev:
        find_nodes(parents, ans, node.left, node, depth + 1, k)
    if node.right != prev:
        find_nodes(parents, ans, node.right, node, depth + 1, k)

    # * 向上查找
    if parents.get(node.val) != prev:
        find_nodes(parents, ans, parents.get(node.val), node, depth + 1, k)


if __name__ == "__main__":
    test_root = TreeNode(3)

    test_root.left = TreeNode(5)
    test_root.left.left = TreeNode(6)
    test_root.left.right = TreeNode(2)
    test_root.left.right.left = TreeNode(7)
    test_root.left.right.right = TreeNode(4)

    test_root.right = TreeNode(1)
    test_root.right.left = TreeNode(0)
    test_root.right.right = TreeNode(8)

    test_target = test_root.left

    print(find_distance_k_nodes(test_root, test_target, 2))
