class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''A simple solution.'''
    
    def height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.height(node.left), self.height(node.right))
    
    def is_balanced(self, root):
        if root is None:
            return True
        delta_height = abs(self.height(root.left) - self.height(root.right))
        left_is_balanced = self.is_balanced(root.left)
        right_is_balanced = self.is_balanced(root.right)
        return delta_height <= 1 and left_is_balanced and right_is_balanced
