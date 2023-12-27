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


def main(postorder: List[int], inorder: List[int]):
    """从中后序数组重建二叉树
    - 递归版本
    - 栈版本

    具体步骤
    - 在中序遍历中定位到根节点，分别获取左右子树节点数目

    Args:
        - root (TreeNode | None): 根节点
    """
    ans = recover_tree_recur(postorder, inorder)
    print(ans)


def recover_tree_recur(
    postorder: List[int],
    inorder: List[int],
) -> TreeNode | None:
    """从中后序数组重建二叉树

    Args:
        - postorder (List[int]): 后序遍历数组
        - inorder (List[int]): 中序遍历数组

    Returns:
        - TreeNode | None: 二叉树根节点
    """
    size = len(postorder)

    # * 为更快找中序遍历的根节点位置，将中序遍历的节点与位置记录成哈希表
    index_map = {v: i for i, v in enumerate(inorder)}

    return construct_tree(
        postorder,
        index_map,
        0,
        size - 1,
        0,
        size - 1,
    )


def construct_tree(
    postorder: List[int],
    index_map: Dict[int, int],
    postorder_left: int,
    postorder_right: int,
    inorder_left: int,
    inorder_right: int,
) -> TreeNode | None:
    """递归构建函数

    Args:
        - postorder (List[int]): 后序遍历数组
        - index_map (Dict[int, int]): 中序遍历节点值和位置的映射关系
        - postorder_left (int): 后序遍历数组的左边界
        - postorder_right (int): 后序遍历数组的右边界
        - inorder_left (int): 中序遍历数组的左边界
        - inorder_right (int): 中序遍历数组的右边界

    Returns:
        - TreeNode | None: 构建的树
    """
    if postorder_left > postorder_right:
        return None

    # * 后序遍历的最后一个元素即为根节点
    postorder_root = postorder_right
    root = TreeNode(postorder[postorder_root])

    # * 从中序遍历哈希表中获取根节点位置
    inorder_root = index_map[postorder[postorder_right]]

    # * 根节点左侧的数组属于左子树，根据左侧区间的长度切割后序遍历数组
    size_left_subtree = inorder_root - inorder_left

    # * 递归构建左右子树
    root.left = construct_tree(
        postorder,
        index_map,
        postorder_left,
        postorder_left + size_left_subtree - 1,
        inorder_left,
        inorder_root - 1,
    )
    root.right = construct_tree(
        postorder,
        index_map,
        postorder_left + size_left_subtree,
        postorder_right - 1,
        inorder_root + 1,
        inorder_right,
    )

    return root


if __name__ == "__main__":
    test_inorder = [4, 2, 5, 1, 6, 3, 7]
    test_postorder = [4, 5, 2, 6, 7, 3, 1]
    main(test_postorder, test_inorder)
