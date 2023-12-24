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


def main(root: TreeNode | None, sub_root: TreeNode | None):
    """判断二叉树子树

    Args:
        - root (TreeNode | None): 根节点
    """
    ans = (root, sub_root)
    print(ans)


def is_sub_tree(root: TreeNode | None, sub_root: TreeNode | None) -> bool:
    """判断子树递归函数

    Args:
        root (TreeNode | None): 二叉树1的根节点
        sub_root (TreeNode | None): 二叉树2的根节点

    Returns:
        bool: 是否2是1的子树
    """
    if not root and not sub_root:
        return True
    if not root or not sub_root:
        return False

    # * 首先判断两棵树是否相同
    is_same = is_same_tree(root, sub_root)

    # * 再递归判断 sub_root 是否是左右子树的子树
    left_is_sub_tree = is_sub_tree(root.left, sub_root)
    right_is_sub_tree = is_sub_tree(root.right, sub_root)

    return is_same or left_is_sub_tree or right_is_sub_tree


def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    """判断二叉树是否相同

    Args:
        p (TreeNode | None): 二叉树根节点1
        q (TreeNode | None): 二叉树根节点2

    Returns:
        bool: 结果
    """
    # * 两个节点都为空则相同
    if not p and not q:
        return True

    # * 两个节点有一个为空则不相同
    if not p or not q:
        return False

    # * 判断节点的值是否相同
    val_is_same = p.val == q.val

    # * 递归判断左右子树是否相同
    left_is_same = is_same_tree(p.left, q.left)
    right_is_same = is_same_tree(p.right, q.right)

    return val_is_same and left_is_same and right_is_same
