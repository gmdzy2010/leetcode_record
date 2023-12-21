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


def main(root: TreeNode | None) -> List[int]:
    """二叉树前序遍历

    Args:
        root (TreeNode | None): 根节点

    Returns:
        List[int]: 前序遍历结果
    """
    ans1: List[int] = []
    preorder_recursively(root, ans1)
    print(ans1)

    ans2 = preorder_stack(root)
    print(ans2)

    return ans1


def preorder_recursively(root: TreeNode | None, ans: List[int]):
    """前序遍历，递归版本

    Args:
        root (TreeNode | None): 根节点
        ans (List[int]): 遍历结果
    """
    if not root:
        return
    ans.append(root.val)
    preorder_recursively(root.left, ans)
    preorder_recursively(root.right, ans)


def preorder_stack(root: TreeNode | None) -> List[int]:
    """前序遍历，非递归版本

    使用栈处理，步骤
    - 根节点先入栈
    - 出栈并处理
    - 右节点入栈
    - 左节点入栈

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
    stack.append(root)
    while stack:
        # * 出栈
        curr = stack.pop()

        # * 处理
        ans.append(curr.val)

        # * 右节点先入栈，左节点再入栈
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

    return ans


if __name__ == "__main__":
    test_root = TreeNode(1)
    test_root.right = TreeNode(2)
    test_root.right.left = TreeNode(3)
    print(main(test_root))
