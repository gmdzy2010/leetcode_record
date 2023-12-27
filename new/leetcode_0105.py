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


def main(preorder: List[int], inorder: List[int]):
    """从前中序数组重建二叉树
    - 递归版本
    - 栈版本

    具体步骤
    - 在中序遍历中定位到根节点，分别获取左右子树节点数目

    Args:
        - root (TreeNode | None): 根节点
    """
    ans = recover_tree_recur(preorder, inorder)
    print(ans)


def recover_tree_recur(
    preorder: List[int],
    inorder: List[int],
) -> TreeNode | None:
    """从前中序数组重建二叉树

    Args:
        - preorder (List[int]): 前序遍历数组
        - inorder (List[int]): 中序遍历数组

    Returns:
        - TreeNode | None: 恢复的二叉树
    """
    size = len(preorder)

    # * 为更快找中序遍历的根节点位置，将中序遍历的节点与位置记录成哈希表
    index_map = {v: i for i, v in enumerate(inorder)}

    return construct_tree(
        preorder,
        index_map,
        0,
        size - 1,
        0,
        size - 1,
    )


def construct_tree(
    preorder: List[int],
    index_map: Dict[int, int],
    preorder_left: int,
    preorder_right: int,
    inorder_left: int,
    inorder_right: int,
) -> TreeNode | None:
    """递归构建函数

    Args:
        - preorder (List[int]): 前序遍历数组
        - index_map (Dict[int, int]): 中序遍历节点值和位置的映射关系
        - preorder_left (int): 前序遍历数组的左边界
        - preorder_right (int): 前序遍历数组的右边界
        - inorder_left (int): 中序遍历数组的左边界
        - inorder_right (int): 中序遍历数组的右边界

    Returns:
        - TreeNode | None: 构建的树
    """
    if preorder_left > preorder_right:
        return None

    # * 前序遍历的第一个元素即为根节点
    preorder_root = preorder_left
    root = TreeNode(preorder[preorder_root])

    # * 从中序遍历哈希表中获取根节点位置
    inorder_root = index_map[preorder[preorder_root]]

    # * 中序遍历的特点，根节点左侧的数组属于左子树
    size_left_subtree = inorder_root - inorder_left

    # * 递归构建左右子树
    root.left = construct_tree(
        preorder,
        index_map,
        preorder_left + 1,
        preorder_left + size_left_subtree,
        inorder_left,
        inorder_root - 1,
    )
    root.right = construct_tree(
        preorder,
        index_map,
        preorder_left + size_left_subtree + 1,
        preorder_right,
        inorder_root + 1,
        inorder_right,
    )

    return root


if __name__ == "__main__":
    test_preorder = [3, 9, 20, 15, 7]
    test_inorder = [9, 3, 15, 20, 7]
    main(test_preorder, test_inorder)
