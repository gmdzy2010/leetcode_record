from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root):
    current_level_nodes, result = deque(), []
    if root:
        current_level_nodes.appendleft(root)
    while current_level_nodes:
        size = len(current_level_nodes)
        for index in range(size):
            node = current_level_nodes[-1]
            current_level_nodes.pop()
            if index == size - 1:
                result.append(node.val)
            if node.left:
                current_level_nodes.appendleft(node.left)
            if node.right:
                current_level_nodes.appendleft(node.right)
    return result
