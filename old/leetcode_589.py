class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def preorder(root):
    if not root:
        return []
    stack, result = [], []
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.val)
        for sub_node in node.children[::-1]:
            stack.append(sub_node)
    return result
