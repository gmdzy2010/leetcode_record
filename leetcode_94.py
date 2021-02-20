class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root):
    stack, result = [], []
    current = root
    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack[-1]
            stack.pop()
            result.append(current.val)
            current = current.right
    return result
