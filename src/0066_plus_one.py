class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #completed on 3/26/2023

        i = len(digits) - 1

        while i >= 0:
            # if adding 1 makes 10, must carry the 1
            if digits[i] + 1 == 10:
                digits[i] = 0
                # if the first element then must insert 1 at the beginning of digits to carry 1
                if i == 0:
                    digits.insert(0,1)
                    return digits
                else:
                    i -= 1
            elif digits[i] + 1 < 10:
                digits[i] += 1
                return digits
