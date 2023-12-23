from typing import Self


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


def main(p: TreeNode | None, q: TreeNode | None):
    """判断二叉树是否相同

    Args:
        - root (TreeNode | None): 根节点
    """
    ans = is_same_tree(p, q)
    print(ans)


def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    """判断二叉树是否相同

    Args:
        p (TreeNode | None): 根节点1
        q (TreeNode | None): 根节点2

    Returns:
        bool: 是否相同
    """
    if not p and not q:
        return True
    if not p or not q:
        return False

    val_is_same = p.val == q.val
    left_is_same = is_same_tree(p.left, q.left)
    right_is_same = is_same_tree(p.right, q.right)

    return val_is_same and left_is_same and right_is_same


if __name__ == "__main__":
    test_root_1 = TreeNode(1)
    test_root_1.left = TreeNode(2)
    test_root_1.right = TreeNode(2)
    test_root_1.left.left = TreeNode(3)

    test_root_2 = TreeNode(1)
    test_root_2.left = TreeNode(2)
    test_root_2.right = TreeNode(2)
    test_root_2.left.left = TreeNode(3)
    test_root_2.left.right = TreeNode(4)

    main(test_root_1, test_root_2)
