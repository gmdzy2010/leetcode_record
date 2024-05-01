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
    """二叉树后序遍历

    Args:
        root (TreeNode | None): 根节点

    Returns:
        List[int]: 前序遍历结果
    """
    ans1: List[int] = []
    postorder_recursively(root, ans1)
    print(ans1)

    ans2 = postorder_stack(root)
    print(ans2)

    return ans1


def postorder_recursively(root: TreeNode | None, ans: List[int]):
    """后序遍历，递归版本

    Args:
        root (TreeNode | None): 根节点
        ans (List[int]): 遍历结果
    """
    if not root:
        return
    postorder_recursively(root.left, ans)
    postorder_recursively(root.right, ans)
    ans.append(root.val)


def postorder_stack(root: TreeNode | None) -> List[int]:
    """后序遍历，非递归版本

    使用两个栈处理
    - 控制栈用来控制 左右中 的遍历顺序
    - 收集栈用来收集遍历过程中所有出过栈的操作

    处理步骤
    - 根节点先入控制栈
    - 循环处理控制栈
        - 出控制栈节点进入收集栈
        - 左节点入控制栈
        - 右节点入控制栈
    - 循环处理收集栈，依次出栈处理即可

    Args:
        - root (TreeNode | None): 根节点
        - ans (List[int]): 遍历结果

    Returns:
        List[int]: 前序遍历结果
    """
    ans: List[int] = []
    if not root:
        return ans

    stack: List[TreeNode] = []

    # * 再使用一个临时栈，用来收集刚出栈的节点
    helper_stack: List[TreeNode] = []

    # * 头节点先入栈
    stack.append(root)

    while stack:
        # * 出栈
        curr = stack.pop()

        # * 使用 helper 栈收集刚出栈的节点
        helper_stack.append(curr)

        # * 右节点先入栈，左节点再入栈
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)

    while helper_stack:
        ans.append(helper_stack.pop().val)

    return ans


if __name__ == "__main__":
    test_root = TreeNode(1)
    test_root.right = TreeNode(2)
    test_root.right.left = TreeNode(3)
    print(main(test_root))
