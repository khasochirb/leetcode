# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        \\\
        :type root: TreeNode
        :rtype: int
        \\\
        height = 0
        if not root:
            height += 0
        else:
            height = 1
            height += max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        return height