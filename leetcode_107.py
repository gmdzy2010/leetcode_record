from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root):
    current_level_nodes, result = deque(), []
    if root:
        current_level_nodes.appendleft(root)
    while current_level_nodes:
        size = len(current_level_nodes)
        sub_level_values = []
        for index in range(size):
            node = current_level_nodes[-1]
            current_level_nodes.pop()
            sub_level_values.append(node.val)
            if node.left:
                current_level_nodes.appendleft(node.left)
            if node.right:
                current_level_nodes.appendleft(node.right)
        result.append(sub_level_values)
    return result[::-1]
