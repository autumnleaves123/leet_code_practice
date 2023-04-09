class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # completed 3/26/2023

        # my solution, which I'm surprised was as fast as it was. Is it O(logN)?
        for i in range(len(nums)):
            curr_num = nums[i]
            #if current num is target, then target is found at index i
            if curr_num == target:
                return i
            #if current num is greater than target, then target does not exist in nums
            #target would be found between indices i-1 and i
            elif curr_num > target:
                return i
        return len(nums)

        # binary search solution. Mine was faster than this?
        # I don't understand... binary search should be much shorter
        #low, high = 0, len(nums)
        #while low < high:
            #mid = (low + high) // 2
            #if target > nums[mid]:
                #low = mid + 1
            #else:
                #high = mid
        #return low
