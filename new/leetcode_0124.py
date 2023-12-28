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


class Solution:
    """_summary_"""

    def __init__(self):
        self.max_sum = float("-inf")

    def get_max_path_sum(self, root: TreeNode | None) -> int | float:
        """获取最大路径和

        Args:
            - root (TreeNode | None): 根节点

        Returns:
            - int | float: 最大路径和
        """
        self.get_max_gain(root)

        return self.max_sum

    def get_max_gain(self, node: TreeNode | None) -> int | float:
        """获取左右子树中的最大贡献值

        Args:
            - node (TreeNode | None): 当前节点

        Returns:
            - int | float: 左右子树中的最大贡献值
        """
        if not node:
            return 0

        # * 左子树的最大贡献值
        # ! 注意这里左子树的最大贡献需要和0比较
        # 只有在最大贡献值大于 0 时，才会选取对应子节点
        left_gain = max(self.get_max_gain(node.left), 0)
        right_gain = max(self.get_max_gain(node.right), 0)

        # * 经过当前节点的贡献值
        gain_with_node = node.val + left_gain + right_gain

        self.max_sum = max(self.max_sum, gain_with_node)

        # * 由于递归计算需要左右子树最大的一个，返回节点值和最大的子树贡献值的和
        return node.val + max(left_gain, right_gain)
