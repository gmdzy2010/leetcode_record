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


def get_num_of_bst(n: int) -> int | float:
    """不同的BST个数

    卡塔兰数
    - G(n): 长度为 n 的序列能构成的不同二叉搜索树的个数
    - F(i, n): 以 i 为根、序列长度为 n 的不同二叉搜索树个数 (1 <= i <= n)

    根据推导存在：
    - F(i, n) = G(i − 1) * G(n − i)
        - i − 1 -> 以 i 为根的左子树节点个数
        - n - i -> 以 i 为根的右子树节点个数
    - 说明 F(i, n) 取决于左/右子树节点能构成的二叉搜索树个数

    对整个序列上的 F(i, n) 求和即可得到 G(n)

    Args:
        - n (int): 有序数组长度

    Returns:
        - int | float: 个数
    """
    G = [0] * (n + 1)

    # * 根节点为空和只有根节点都可以有一个树
    G[0], G[1] = 1, 1

    for i in range(2, n + 1):
        for j in range(1, i + 1):
            G[i] += G[j - 1] * G[i - j]

    return G[n]


if __name__ == "__main__":
    get_num_of_bst(4)
