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


def main(root: TreeNode | None):
    """判断二叉树是否对称

    Args:
        - root (TreeNode | None): 根节点

    Returns:
        - bool: 是否对称的结果
    """
    ans1 = is_symmetry_recursively(root)
    print(ans1)

    ans2 = is_symmetry_stack(root)
    print(ans2)

    ans3 = is_symmetry_queue(root)
    print(ans3)


def is_symmetry_stack(root: TreeNode | None) -> bool:
    """判断二叉树是否对称，栈版本

    Args:
        - root (TreeNode | None): 根节点

    Returns:
        - bool: 是否对称的结果
    """
    if not root:
        return True

    # * 使用一个栈存储将要比对的节点
    stack: List[TreeNode | None] = []

    # * 左节点入栈，然后右节点入栈
    stack.append(root.left)
    stack.append(root.right)

    while stack:
        right = stack.pop()
        left = stack.pop()

        # ! 这个判断一定要放在前面
        if not left and not right:
            continue

        if not left or not right or (left.val != right.val):
            return False

        # * 后续节点再次入栈，内外侧节点对入栈顺序要和 上文的出栈顺序相反
        # 子树外侧比较：左 -> 左节点 vs 右 -> 右节点，入栈顺序不能变
        stack.append(left.left)
        stack.append(right.right)

        # 子树内侧比较：右 -> 左节点 vs 左 -> 右节点，入栈顺序不能变
        stack.append(right.left)
        stack.append(left.right)

    return True


def is_symmetry_queue(root: TreeNode | None) -> bool:
    """判断二叉树是否对称，队列版本

    Args:
        - root (TreeNode | None): 根节点

    Returns:
        - bool: 是否对称的结果
    """
    if not root:
        return True

    # * 使用一个栈存储将要比对的节点
    queue: Deque[TreeNode | None] = deque()

    # * 左节点入栈，然后右节点入栈
    queue.appendleft(root.left)
    queue.appendleft(root.right)
    while queue:
        left = queue.pop()
        right = queue.pop()

        # ! 这个判断一定要放在前面
        if not left and not right:
            continue

        if not left or not right or (left.val != right.val):
            return False

        # * 后续节点再次入栈
        queue.appendleft(right.left)
        queue.appendleft(left.right)

        queue.appendleft(left.left)
        queue.appendleft(right.right)

    return True


def is_symmetry_recursively(root: TreeNode | None) -> bool:
    """判断二叉树是否对称，递归版本

    Args:
        - root (TreeNode | None): 根节点

    Returns:
        - bool: 是否对称的结果
    """
    if not root:
        return True

    return compare(root.left, root.right)


def compare(left: TreeNode | None, right: TreeNode | None) -> bool:
    """对称比对的递归函数

    Args:
        left (TreeNode | None): 左节点
        right (TreeNode | None): 右节点

    Returns:
        bool: 比较结果
    """
    # * 左右节点皆为空，对称
    if not left and not right:
        return True

    # * 左右节点其中一个为空，不对称
    if (left and not right) or (not left and right):
        return False

    # * 左右节点均不为空，进入下一次递归过程
    if left and right:
        # * 左右节点值不相同，不对称
        if left.val != right.val:
            return False

        # * 分别计算内侧的子树和外侧的子树是否对称
        outside = compare(left.left, right.right)
        inside = compare(left.right, right.left)

        return outside and inside

    return False


if __name__ == "__main__":
    test_root = TreeNode(1)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(2)
    test_root.left.left = TreeNode(3)
    test_root.left.right = TreeNode(4)
    test_root.right.left = TreeNode(4)
    test_root.right.right = TreeNode(3)
    main(test_root)
