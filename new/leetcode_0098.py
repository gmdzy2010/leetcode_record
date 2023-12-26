from typing import List, Self


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
        return f"_ <- node: {self.val} -> _"


def main(root: TreeNode | None):
    """验证二叉搜索树
    - 递归版本
    - 迭代版本

    Args:
        root (TreeNode | None): 根节点
    """
    ans1 = is_valid_bst_recur(root)
    print(ans1)

    ans2 = is_valid_bst_stack(root)
    print(ans2)


def is_valid_bst_recur(root: TreeNode | None) -> bool:
    """验证二叉搜索树（BST），递归版本

    利用二叉搜索树的中序遍历得到的列表为有序，来验证是否是合格的

    Args:
        - root (TreeNode | None): 根节点

    Returns:
        - bool: 是否是二叉搜索树
    """
    if not root:
        return False

    res: List[int] = []
    inorder_transversal(root, res)
    for i in range(1, len(res)):
        if res[i] <= res[i - 1]:
            return False

    return True


def inorder_transversal(root: TreeNode | None, res: List[int]):
    """二叉树中序遍历

    Args:
        root (TreeNode | None): 根节点
        res (List[int]): 遍历结果列表
    """
    if not root:
        return

    inorder_transversal(root.left, res)
    res.append(root.val)
    inorder_transversal(root.right, res)


def is_valid_bst_stack(root: TreeNode | None) -> bool:
    """验证二叉搜索树（BST），栈版本

    Args:
        - root (TreeNode | None): 根节点

    Returns:
        - bool: 是否是二叉搜索树
    """
    stack: List[TreeNode] = []

    # * 记录当前节点
    curr: TreeNode | None = root

    # * 记录上一个节点，比较值大小需要
    prev: TreeNode | None = None
    while curr or stack:
        # ? 这里没懂
        if curr:
            stack.append(curr)

            # * 左节点入栈
            curr = curr.left
        else:
            curr = stack.pop()

            # * 看看中间节点的值是不是比左节点大
            if prev and curr.val <= prev.val:
                return False

            prev = curr

            # * 走到下一个右节点，下次出栈的仍然是右节点
            curr = curr.right

    return True


if __name__ == "__main__":
    test_root_1 = TreeNode(4)

    test_root_1.left = TreeNode(3)
    test_root_1.left.left = TreeNode(1)
    test_root_1.left.right = TreeNode(2)

    test_root_1.right = TreeNode(6)
    test_root_1.right.left = TreeNode(5)
    test_root_1.right.right = TreeNode(7)

    main(test_root_1)
