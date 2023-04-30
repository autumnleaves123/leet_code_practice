class Solution:
    def sumOfMultiples(self, n: int) -> int:

        # completed on 4/23/2023
        # O(1) run time using the summation rule where sum of 1 to n is n(n+1)/2

        # subtract duplicates
        # add back in numbers that are multiples of 3, 5, and 7 (multiple of 105)
        sum = 3*self.sumN(n//3) + 5*self.sumN(n//5) + 7*self.sumN(n//7) - 15*self.sumN(n//15) - 21*self.sumN(n//21) - 35*self.sumN(n//35) + 105*self.sumN(n//105)
        
        return int(sum)

    def sumN (self, n:int) -> int:
        return n * (n+1) / 2
