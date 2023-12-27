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


def main(root: TreeNode | None):
    """路径总和

    Args:
        - root (TreeNode | None): 根节点
    """
    ans1 = get_path_recur(root)
    print(ans1)

    ans2 = get_path_stack(root)
    print(ans2)


def get_path_recur(root: TreeNode | None) -> List[str]:
    """获取所有路径，递归版本

    Args:
        - root (TreeNode | None): 根节点

    Returns:
        - List[str]: 所有路径的字符串表示
    """
    ans: List[str] = []
    visited_path = ""
    if not root:
        return ans

    transversal(root, visited_path, ans)

    return ans


def transversal(node: TreeNode, visited_path: str, ans: List[str]):
    """路径回溯（递归）函数

    Args:
        node (TreeNode): 当前节点，注意不为空
        visited_path (str): 已经经过的路径
        ans (List[str]): 路径结果
    """
    visited_path += str(node.val)

    # * 左右节点为空时，停止回溯（即回到上一层函数，也回到父节点），结果列表记录下当前节点
    if not node.left and not node.right:
        ans.append(visited_path)
        return

    # * 只要左右节点有一个不为空，就继续向下找
    if node.left:
        transversal(node.left, visited_path + "->", ans)
    if node.right:
        transversal(node.right, visited_path + "->", ans)


def get_path_stack(root: TreeNode | None) -> List[str]:
    """获取所有路径，栈版本

    Args:
        - root (TreeNode | None): 根节点

    Returns:
        - List[str]: 所有路径的字符串表示
    """
    ans: List[str] = []
    if not root:
        return ans

    stack: List[Tuple[TreeNode, str]] = []

    # * 记住初始化的时候，还没有“经过”根节点，所以路径为空
    stack.append((root, ""))
    while stack:
        node, curr_path = stack.pop()

        # * 经过了当前节点，需要记录下来经过的路径
        if not curr_path:
            curr_path = f"{node.val}"
        else:
            curr_path = f"{curr_path}->{node.val}"

        # * 左右节点都为空，开始结算路径
        if not node.left and not node.right:
            ans.append(curr_path)

        if node.left:
            stack.append((node.left, curr_path))
        if node.right:
            stack.append((node.right, curr_path))

    return ans


if __name__ == "__main__":
    test_root = TreeNode(1)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(3)
    test_root.left.left = TreeNode(4)
    test_root.left.right = TreeNode(5)
    test_root.right.left = TreeNode(6)
    test_root.right.right = TreeNode(7)
    main(test_root)
