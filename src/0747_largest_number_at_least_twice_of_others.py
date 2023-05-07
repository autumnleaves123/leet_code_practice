class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        # Completed on 5/7/2023

        max_idx = 0
        max_val = 0
        nxt_max_val = 0

        for i in range(len(nums)):
            if nums[i] >= max_val:
                nxt_max_val = max_val
                max_val = nums[i]
                max_idx = i
            else:
                nxt_max_val = max(nums[i],nxt_max_val)
        
        if max_val >= 2*nxt_max_val:
            return max_idx
        else:
            return -1