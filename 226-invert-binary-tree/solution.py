# https://leetcode.com/problems/invert-binary-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """Given the root of a binary tree, invert the tree, and return its root."""

    def invertTree(self, root: TreeNode):
        if root is None:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # recursively call your self to swap left and right
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

tree = TreeNode(4)
tree.left = TreeNode(2)
tree.right = TreeNode(7)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(9)

s = Solution()
s.invertTree(tree)
