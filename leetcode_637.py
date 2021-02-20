from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def average_of_levels(root):
    current_level_nodes, result = deque(), []
    if root:
        current_level_nodes.appendleft(root)
    while current_level_nodes:
        size, level_value_sum = len(current_level_nodes), 0
        for index in range(size):
            node = current_level_nodes[-1]
            current_level_nodes.pop()
            level_value_sum += node.val
            if node.left:
                current_level_nodes.appendleft(node.left)
            if node.right:
                current_level_nodes.appendleft(node.right)
        result.append(level_value_sum / size)
    return result
