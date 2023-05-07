# Import math Library
import math 

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:

        # Redid on 5/7/2023 for a O(NlogN) solution
        # After discussing with Daryl in Saturday session
        
        # stores all the multiples we've seen
        mult = []

        # iterate through list - O(N)
        for num in nums:

            #adding any multiple that are a power of 2 to the list
            if num % original == 0 and (math.log(num//original,2) == math.floor(math.log(num//original,2)) or num == original):
                mult.append(num)
        
        # sort list - O(NlogN)
        mult.sort()
        
        # iterate thorugh sorted list - O(N)
        for i in range(0,len(mult)):
            # repeat value, we have already found this value so can continue
            if i > 0 and mult[i] == mult[i-1]:
                continue
            # found value, double original
            elif mult[i] == original:
                original *= 2
            # did not find value, stop loop
            else:
                break

        return original