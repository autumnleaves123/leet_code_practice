class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # completed 3/26/2023
        # redid incorporating tips from a solution

        n_not_val = 0
        for num in nums:
            if num != val:
                nums[n_not_val] = num
                n_not_val += 1
        return n_not_val
