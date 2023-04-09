class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #completed 3/23/2023

        #my solution uses python, very clean
        #try:
        #    return haystack.index(needle)
        #except:
        #    return -1

        #example optimization
        first_occ = -1
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i] != needle[0]:
                continue
            if haystack[i:i+len(needle)] == needle:
                first_occ = i
                break
        return first_occ
