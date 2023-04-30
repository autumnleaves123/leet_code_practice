# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        return self.isBalancedHeight(root)[1]

    def isBalancedHeight(self, node: Optional[TreeNode]) -> (int,bool):
        k = 1

        if not node:
            return (0,True)
        
        right = self.isBalancedHeight(node.right)
        if not right[1]:
            return (0,False)
        left = self.isBalancedHeight(node.left)

        right_height = right[0]
        left_height = left[0]
        node_height = max(right_height,left_height) + 1
        height_diff = abs(right_height - left_height)

        right_isBalanced = right[1]
        left_isBalanced = left[1]

        # if either left or right subtree is unbalanced, return false
        if not right_isBalanced or not left_isBalanced:
            return (node_height,False)
        # if both left or right subtree is unbalanced and height difference is greater than k
        elif height_diff > k:
            return (node_height,False)
        else:
            return (node_height,True)