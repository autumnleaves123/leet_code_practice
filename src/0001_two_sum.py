class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #define hashmap
        idx_by_val = {}

        #cycle through elements in nums List
        for i in range(len(nums)):

            #value of element in nums List at index i
            val = nums[i]

            #value needed to add up to target.
            #will use this value to search hashmap
            val_needed = target - val

            #if val_needed exists in hashmap, then index is known
            #for value needed for current val to add up to target
            if val_needed in idx_by_val:

                #return current index and index of val_needed
                return [i,idx_by_val[val_needed]]

            #save current position i and value to hashmap
            idx_by_val[val] = i
