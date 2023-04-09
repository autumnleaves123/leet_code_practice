# completed on 3/26/2023
# example solution that has fastest run time, had to optimize to include case where r == 1
"""def binary_search(l, r, target):
    if r == l or r == 1: # accounting for 0 and 1 case
        return r
    elif r - l == 1:
        return min(r,l)
    m = (r + l) // 2
    if m * m > target:
        return binary_search(l, m, target)
    else:
        return binary_search(m, r, target)

class Solution:
    def mySqrt(self, x: int) -> int:
        return binary_search(0, x, x)
"""

# my solution is simpler, but way slower because it goes through every number up to x+ 1
# uses concepts from LeetCode Problem 35. Search Insert Position
class Solution:
    def mySqrt(self, x: int) -> int:

        for i in range(x+1):
            if i*i == x:
                return i
            elif i*i > x:
                return i-1
            continue
        return 0
