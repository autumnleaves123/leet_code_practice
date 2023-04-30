# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        # completed 4/22/2023 in Flo's easy LeetCode
        length = len(nums)

        # base condition 1: nums is empty array
        if length == 0:
            return None
        # base condition 2: nums only has one element
        elif length == 1:
            return TreeNode(nums[0],None,None)
        else:
            mid = length // 2
            return TreeNode(nums[mid],self.sortedArrayToBST(nums[0:mid]),self.sortedArrayToBST(nums[(mid+1):length]))

