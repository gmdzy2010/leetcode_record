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
        if self.left and not self.right:
            return f"{self.left} <- node: {self.val} -> _"
        if not self.left and self.right:
            return f"_ <- node: {self.val} -> {self.right}"
        return f"_ <- node: {self.val} -> _"


def main(root: TreeNode | None) -> List[int]:
    """二叉树中序遍历

    Args:
        root (TreeNode | None): 根节点

    Returns:
        List[int]: 前序遍历结果
    """
    ans1: List[int] = []
    inorder_recursively(root, ans1)
    print(ans1)

    ans2 = inorder_stack(root)
    print(ans2)

    return ans1


def inorder_recursively(root: TreeNode | None, ans: List[int]):
    """中序遍历，递归版本

    Args:
        root (TreeNode | None): 根节点
        ans (List[int]): 遍历结果
    """
    if not root:
        return
    inorder_recursively(root.left, ans)
    ans.append(root.val)
    inorder_recursively(root.right, ans)


def inorder_stack(root: TreeNode | None) -> List[int]:
    """中序遍历，非递归版本

    使用栈处理，步骤
    - 左边界不断入栈
    - 当左边界到达最下方，开始出栈处理
    - 到右孩子入栈，再处理下一层左边界
    - 重复以上过程

    Args:
        root (TreeNode | None): 根节点
        ans (List[int]): 遍历结果

    Returns:
        List[int]: 前序遍历结果
    """
    ans: List[int] = []
    if not root:
        return ans

    stack: List[TreeNode] = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            ans.append(root.val)
            root = root.right

    return ans


if __name__ == "__main__":
    test_root = TreeNode(1)
    test_root.right = TreeNode(2)
    test_root.right.left = TreeNode(3)
    print(main(test_root))
