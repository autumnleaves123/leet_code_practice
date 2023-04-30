# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        # completed on 4/22
        
        # accounting for case where binary tree is null
        if not root:
            return 0
        
        # no more left branch in binary tree
        # cannot take min because min of 0 and anything else is 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        # no more right branch
        elif not root.right:
            return 1 + self.minDepth(root.left)

        # keep track of level and then traverse tree, but only add largest between left and right
        return 1 + min(self.minDepth(root.left),self.minDepth(root.right))