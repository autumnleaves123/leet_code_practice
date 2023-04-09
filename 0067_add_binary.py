class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # completed on 3/26/2023

        bin = ""
        carry = 0
        i = 0
        while i < max(len(a),len(b)):
            if i >= len(a): #end of a
                sum = int(b[len(b)-1-i]) + carry
            elif i >= len(b): #end of b
                sum = int(a[len(a)-1-i]) + carry
            else:
                sum = int(a[len(a)-1-i]) + int(b[len(b)-1-i]) + carry
            digit = sum % 2
            carry = sum//2
            bin = str(digit) + bin
            i += 1

        if carry > 0:
            bin = str(carry) + bin

        return bin
