class Solution:
    def isPalindrome(self, x: int) -> bool:

        # recursion base case: negative numbers can never be palindromes
        if x < 0:
            return False
        # recursion base case: any number x with 1 or 0 digits is a palindrome
        elif x < 10:
            return True
        # compare first and last digit if x has more than 1 digits
        else: # x >= 10
            # extract last digit
            last_digit = x % 10

            # extract first digit by determining how long number is
            places_x = 0
            dummy_x = x
            while dummy_x > 9:
                places_x += 1
                dummy_x = dummy_x // 10 #floor division to keep int type

            first_digit = x // 10**places_x

            middle_digits = (x - first_digit * 10**places_x) // 10

            places_mid = 0
            dummy_mid = middle_digits
            while dummy_mid > 9:
                places_mid += 1
                dummy_mid = dummy_mid // 10 #floor division to keep int type

            leading_zeros = places_x - places_mid - 2

            if leading_zeros > 0:
                if middle_digits % 10**leading_zeros != 0:
                    return False
                else:
                    return True and self.isPalindrome(middle_digits% 10**leading_zeros)

            # if first digit and last digit are equal,
            # complete the same test after removing first and last digits
            elif first_digit == last_digit:
                return True and self.isPalindrome(middle_digits)
            # first digit and last digit are not equal
            else:
                return False
