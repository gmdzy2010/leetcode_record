from typing import List, Self, Tuple


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


def path_target(root: TreeNode | None, target: int) -> List[List[int]]:
    """二叉树路径总和，栈版本

    Args:
        root (TreeNode | None): 根节点
        target (int): 目标值

    Returns:
        List[List[int]]: 路径结果
    """
    ans: List[List[int]] = []
    if not root:
        return ans

    stack: List[Tuple[TreeNode, List[int]]] = []
    stack.append((root, []))
    while stack:
        node, visited_vals = stack.pop()
        visited_vals.append(node.val)

        # * 左右节点都为空，开始结算路径
        if not node.left and not node.right and sum(visited_vals) == target:
            ans.append(visited_vals)

        if node.left:
            stack.append((node.left, visited_vals[:]))
        if node.right:
            stack.append((node.right, visited_vals[:]))

    return ans


if __name__ == "__main__":
    test_root = TreeNode(5)
    test_root.left = TreeNode(4)
    test_root.right = TreeNode(8)
    test_root.left.left = TreeNode(11)
    test_root.left.left.left = TreeNode(7)
    test_root.left.left.right = TreeNode(2)
    test_root.right.left = TreeNode(13)
    test_root.right.right = TreeNode(4)
    print(path_target(test_root, 22))
