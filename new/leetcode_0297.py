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


class Codec:
    """二叉树编解码器"""

    def serialize(self, root: TreeNode | None) -> str:
        """二叉树序列化为字符串

        Args:
            root (TreeNode | None): 根节点

        Returns:
            str: 编码后的字符串
        """
        ans: List[str] = []
        nodes: Deque[TreeNode | None] = deque()
        nodes.appendleft(root)
        while nodes:
            node = nodes.pop()
            if node:
                ans.append(str(node.val))
                nodes.appendleft(node.left)
                nodes.appendleft(node.right)
            else:
                ans.append("null")

        return "[" + ",".join(ans) + "]"

    def deserialize(self, data: str) -> TreeNode | None:
        """从字符串还原二叉树结构

        Args:
            data (str): 二叉树字符串表示

        Returns:
            TreeNode | None: 还原后的二叉树根节点
        """
        if data in ("[]", "[null]"):
            return None

        vals: List[str] = data[1:-1].split(",")
        nodes: Deque[TreeNode] = deque()
        root = TreeNode(int(vals[0]))
        nodes.appendleft(root)

        i = 1
        while nodes:
            node = nodes.pop()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                nodes.appendleft(node.left)
            if vals[i + 1] != "null":
                node.right = TreeNode(int(vals[i + 1]))
                nodes.appendleft(node.right)
            i += 2

        return root
