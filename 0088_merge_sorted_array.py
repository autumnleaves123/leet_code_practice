class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = 0
        i1 = 0
        i2 = 0

        #completed on 4/7/2023

        #if n is 0, then no elements in nums2 and nums1 will not be altered
        if n != 0:
            #if finished iterating through nums2, then finish rest of nums1 is sortedif i2 == n:
            while i2 < n and i < ( n + m ) :
                # if current element in nums1 > nums2, insert nums2 value and increment nums2
                if nums2[i2] < nums1[i] or i1 == m:
                    nums1.insert(i,nums2[i2])
                    nums1.pop() #adding element, so removing last element to maintain length of array
                    i2 += 1
                    i += 1
                # if current element in nums1 < nums2, iterate through nums1
                else:
                    i1 += 1
                    i += 1
