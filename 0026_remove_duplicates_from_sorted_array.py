class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # completed on 3/26/2023

        dict = {}

        unique = 0 #number of unique elements
        i = 0 #iterator through nums List
        while i < len(nums):
            val = nums[i] #value at current array elem
            if val in dict: #value already exists, keep looking for next unique element
                i += 1
            else: #value doesn't already exist, so it is unique
                dict[val] = unique #add to dictionary
                nums[unique] = val #replace array elem at index = unique with curr val
                unique += 1
                i += 1 #look at next element

        return unique
