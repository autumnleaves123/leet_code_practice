class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Completed on 5/1/2023 in Flo's medium rare

        # Given: 2 <= height.length <= 10**5
        max_a_cont = 0

        left = 0 # out left pointer
        right = len(height)-1 # outer right pointer

        while right-left >= 1:
            # LEFT SIDE
            if height[left] < height[right]: # first elem is less than last elem
                max_a_cont = max(height[left] * (right-left),max_a_cont)
                left += 1
            # RIGHT SIDE
            else:
                max_a_cont = max(height[right] * (right-left),max_a_cont)
                right -= 1
        return max_a_cont