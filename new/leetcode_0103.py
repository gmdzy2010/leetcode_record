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


def tranverse_in_zigzag_levelorder_1(root: TreeNode | None) -> List[List[int]]:
    """二叉树的zigzag层序遍历

    从二叉树的层序遍历修改
    - 使用双端队列保存每层的节点的值
        - 当层数是偶数时，节点的值从队列尾部(appendleft)入队
        - 当层数是奇数时，节点的值从队列头部(append)入队

    Args:
        - root (TreeNode | None): 二叉树根节点

    Returns:
        - List[List[int]]: zigzag层序遍历的结果
    """
    ans: List[List[int]] = []
    if not root:
        return ans

    level: int = 0
    nodes: Deque[TreeNode] = deque()
    nodes.appendleft(root)
    while nodes:
        size = len(nodes)
        node_values: Deque[int] = deque()
        for _ in range(size):
            node = nodes.pop()
            if level % 2 == 0:
                node_values.append(node.val)
            else:
                node_values.appendleft(node.val)

            if node.left:
                nodes.appendleft(node.left)
            if node.right:
                nodes.appendleft(node.right)

        ans.append(list(node_values))
        level += 1

    return ans


def tranverse_in_zigzag_levelorder_2(root: TreeNode | None) -> List[List[int]]:
    """二叉树的zigzag层序遍历

    从二叉树的层序遍历，直接反转每层的列表即可

    Args:
        - root (TreeNode | None): 二叉树根节点

    Returns:
        - List[List[int]]: zigzag层序遍历的结果
    """
    ans: List[List[int]] = []
    if not root:
        return ans

    level: int = 0
    nodes: Deque[TreeNode] = deque()
    nodes.appendleft(root)
    while nodes:
        size = len(nodes)
        node_values: List[int] = []
        for _ in range(size):
            node = nodes.pop()
            node_values.append(node.val)
            if node.left:
                nodes.appendleft(node.left)
            if node.right:
                nodes.appendleft(node.right)

        ans.append(node_values if level % 2 == 0 else node_values[::-1])
        level += 1

    return ans


if __name__ == "__main__":
    test_root = TreeNode(1)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(3)
    test_root.left.left = TreeNode(4)
    test_root.right.right = TreeNode(5)
    print(tranverse_in_zigzag_levelorder_1(test_root))
    print(tranverse_in_zigzag_levelorder_2(test_root))
