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


class TreeVisualizer:
    """二叉树可视化简单实现

    实现来源：
    - https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    """

    def __init__(self, empty_symbol: str = " ", compact: bool = False) -> None:
        self.compact: bool = compact
        self.symbol: str = empty_symbol

    def height(self, node: TreeNode | None) -> int:
        """_summary_

        Args:
            node (TreeNode | None): _description_

        Returns:
            int: _description_
        """
        if not node:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return max(left_height, right_height) + 1

    def left_align(
        self,
        matrix: List[List[str]],
        compact: bool = False,
    ) -> List[List[str]]:
        """_summary_

        Args:
            matrix (List[List[str]]): _description_
            compact (bool, optional): _description_. Defaults to False.

        Returns:
            List[List[str]]: _description_
        """
        # Find the index of the first non-empty column
        empty_columns: List[int] = []
        for col_idx, _ in enumerate(matrix[0]):
            for row_idx, _ in enumerate(matrix):
                symbol = matrix[row_idx][col_idx]
                if symbol == self.symbol or (
                    symbol == "─" if compact else False
                ):
                    continue
                break
            else:
                empty_columns.append(col_idx)

        # Replace space characters with empty strings in empty columns
        for row_idx, _ in enumerate(matrix):
            for col_idx in empty_columns:
                matrix[row_idx][col_idx] = ""

        return matrix

    def display(self, root: TreeNode, compact=False):
        """可视化二叉树

        思路
        - 根据二叉树的高度信息构造一个字符串二维阵列
        - 根据节点父子关系，逐渐生成字符串矩阵的每个位置

        Args:
            - root: (TreeNode): 二叉树根节点
            - compact (bool, optional): 显示是否紧凑，默认非紧凑
        """
        # * 计算树的高度
        H = self.height(root)

        # * 整体打印的是一个字符串矩阵
        matrix: List[List[str]] = [
            [self.symbol] * (2**H) * 2 for _ in range(H * 2)
        ]
        col_idx: int = 2**H
        levels: List[List[Tuple[TreeNode, int]]] = [[(root, col_idx)]]
        for l in range(H):
            curr_lvl = levels[l]
            next_lvl = []
            for node, col_idx in curr_lvl:
                # * matrx 的偶数行是节点值所在行，
                matrix[l * 2][col_idx] = str(node.val)

                # * matrix 的奇数行是连接父子节点的字符串行
                conn_row = matrix[l * 2 + 1]

                # * 处理
                if node.left:
                    lft_idx = col_idx - 2 ** (H - l - 1)
                    next_lvl.append((node.left, lft_idx))
                    # connector row for children
                    conn_row[col_idx] = "┘"
                    conn_row[lft_idx] = "┌"
                    for j in range(lft_idx + 1, col_idx):
                        conn_row[j] = "─"

                if node.right:
                    rt_idx = col_idx + 2 ** (H - l - 1)
                    next_lvl.append((node.right, rt_idx))
                    conn_row[col_idx] = "└"
                    conn_row[rt_idx] = "┐"
                    for j in range(col_idx + 1, rt_idx):
                        conn_row[j] = "─"

                if node.left and node.right:
                    conn_row[col_idx] = "┴"

            levels.append(next_lvl)

        matrix = self.left_align(matrix, compact)
        for row in matrix:
            print("".join(row))


if __name__ == "__main__":
    test_root = TreeNode(4)
    test_root.left = TreeNode(2)
    test_root.left.left = TreeNode(1)
    test_root.left.left.left = TreeNode(0)
    test_root.left.left.right = TreeNode(9)
    test_root.left.right = TreeNode(3)
    test_root.right = TreeNode(7)
    test_root.right.left = TreeNode(6)
    test_root.right.right = TreeNode(8)
    test_root.right.right.left = TreeNode(3)
    test_root.right.right.right = TreeNode(4)

    visualizer = TreeVisualizer(empty_symbol=" ")
    visualizer.display(test_root)
