from math import factorial

class Solution:
    def climbStairs(self, n: int) -> int:
        # I had been working on this for a while, but finished on 4/7/2023 in TSU interview prep class with Kevin
        ways = 0

        # where n2 is number of times you climb 2 steps, max is n steps divided by 2
        for n2 in range(0,n//2+1):
            # where n1 is number of times you climb 1 step
            n1 = n - 2*n2
            # mississippi rule
            ways += factorial(n1 + n2) / factorial(n1) / factorial(n2)

        # factorial function returns a float
        return int(ways)
