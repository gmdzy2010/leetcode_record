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


def main(root: TreeNode | None, target_path_sum: int):
    """路径总和

    Args:
        - root (TreeNode | None): 根节点
    """
    ans1 = has_sum_path_recur(root, target_path_sum)
    print(ans1)

    ans2 = has_sum_path_stack(root, target_path_sum)
    print(ans2)


def has_sum_path_recur(root: TreeNode | None, target_path_sum: int) -> bool:
    """判断路径总和，递归版本

    Args:
        root (TreeNode | None): 根节点
        target_path_sum (int): 目标路径总和

    Returns:
        bool: 是否存在
    """
    if not root:
        return False

    # * 到达叶子节点，结算路径和是否等于target
    if not root.left and not root.right:
        return target_path_sum == root.val

    # * 分别在左右子树找是否存在 targetSum - root.val 的路径
    left_has_sum = has_sum_path_recur(root.left, target_path_sum - root.val)
    right_has_sum = has_sum_path_recur(root.right, target_path_sum - root.val)

    return left_has_sum or right_has_sum


def has_sum_path_stack(root: TreeNode | None, target_path_sum: int) -> bool:
    """判断路径总和，栈版本

    Args:
        root (TreeNode | None): 根节点
        target_path_sum (int): 目标路径总和

    Returns:
        bool: 是否存在目标路径总和为 target_path_sum 的路径
    """
    if not root:
        return False

    # * 使用栈记录当前节点和当前的节点值累加和
    stack: List[Tuple[TreeNode, int]] = []
    stack.append((root, root.val))
    while stack:
        node, curr_sum = stack.pop()

        # * 当前节点的左右节点为空且累加和等于目标值，找到了目标路径
        if not node.left and not node.right and target_path_sum == curr_sum:
            return True

        # * 继续往下找
        if node.left:
            stack.append((node.left, curr_sum + node.left.val))
        if node.right:
            stack.append((node.right, curr_sum + node.right.val))

    return False


if __name__ == "__main__":
    test_root = TreeNode(1)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(3)
    test_root.left.left = TreeNode(4)
    test_root.left.right = TreeNode(5)
    test_root.right.left = TreeNode(6)
    test_root.right.right = TreeNode(7)
    main(test_root, 7)
