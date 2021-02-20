from collections import deque


def invert_tree_recursion(root):
    if not root:
        return root
    root.left, root.right = root.right, root.left
    invert_tree_recursion(root.left)
    invert_tree_recursion(root.right)
    return root


def invert_tree_preorder(root):
    if not root:
        return root
    stack = [root]
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return root


def invert_tree_level_order(root):
    current_level_nodes, result = deque(), []
    if root:
        current_level_nodes.appendleft(root)
    while current_level_nodes:
        size = len(current_level_nodes)
        for index in range(size):
            node = current_level_nodes[-1]
            current_level_nodes.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                current_level_nodes.appendleft(node.left)
            if node.right:
                current_level_nodes.appendleft(node.right)
    return root
