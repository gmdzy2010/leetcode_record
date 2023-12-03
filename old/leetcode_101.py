class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def compare(left, right):
    if left and not right:
        return False
    elif not left and right:
        return False
    elif not left and not right:
        return True
    elif left.val != right.val:
        return False
    outside = compare(left.left, right.right)
    inside = compare(left.right, right.left)
    return outside and inside


def is_symmetric(root):
    if not root:
        return True
    return compare(root.left, root.right)
