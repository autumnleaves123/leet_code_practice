# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Jupyter notebook documentation available
        
        # accounting for case where binary tree is null
        if not root:
            return 0

        # keep track of level and then traverse tree, but only add largest between left and right
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
