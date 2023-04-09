# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # completed on 4/8/2023 in easy-leet-code-problems with Flo

        # either p or q are leaves
        if not p and not q:
            return True

        elif not p or not q:
            return False

        # p or q are not leaves
        return p.val == q. val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
