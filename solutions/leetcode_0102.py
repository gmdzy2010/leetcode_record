from collections import deque
from typing import Deque, List, Self


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


def tranverse_in_levelorder(root: TreeNode | None) -> List[List[int]]:
    """二叉树的层序遍历

    宽度优先遍历套路：使用队列
    - 头节点先入队
    - 只要队列不为空，重复执行，对于队列中的每个节点
        - 出队列，对出来的节点进行处理（保存或者打印等）
        - 先左节点入队（如果左节点存在的话），后右节点入队（如果存在的话）
        - 重复以上过程

    Args:
        - root (TreeNode | None): 二叉树根节点

    Returns:
        - List[List[int]]: 层序遍历的结果
    """
    ans: List[List[int]] = []
    if not root:
        return ans

    # * 准备一个队列存储当前成的节点
    nodes: Deque[TreeNode] = deque()

    # * 根节点先入队
    nodes.appendleft(root)

    # * 只要队列中有节点，就重复以下过程：
    # 对于队列中的所有节点，队处理 -> 左节点入队 -> 右节点入队
    while nodes:
        size = len(nodes)
        node_values: List[int] = []

        for _ in range(size):
            node = nodes.pop()
            node_values.append(node.val)
            if node.left:
                nodes.appendleft(node.left)
            if node.right:
                nodes.appendleft(node.right)

        # * 记录当前层级的所有节点值
        ans.append(node_values)

    return ans
