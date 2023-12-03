from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def preorder(root):
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
            for node in node.children:
                current_level_nodes.appendleft(node)
        result.append(sub_level_values)
    return result
