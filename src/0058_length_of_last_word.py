class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #completed on 3/26/2023

        #strip leading and trailing whitespace
        stripped = s.strip()
        i = len(stripped)-1

        while i >= 0:
            if stripped[i] == " ":
                return len(stripped) - i - 1
            i -= 1

        # if no spaces, all of s is a word
        return len(stripped)


        # quickest solution from LeetCode
        #l=s.split()
        #n=len(l)
        #return len(l[n-1])
