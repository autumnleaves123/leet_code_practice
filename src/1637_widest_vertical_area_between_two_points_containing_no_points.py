class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        #completed on 5/6/2023 in Daryl's session
        points.sort()
        result = 0
        for i in range(1, len(points)):
            result = max(result, points[i][0] - points[i-1][0])
        return result