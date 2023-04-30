class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # completed on 4/30/2023
        
        if not root:
            return False
        # found leaf
        elif not root.left and not root.right:
            return targetSum == root.val

        newTargetSum = targetSum - root.val

        return self.hasPathSum(root.left,newTargetSum) or self.hasPathSum(root.right,newTargetSum)