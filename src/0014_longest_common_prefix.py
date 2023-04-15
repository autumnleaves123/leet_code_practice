class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # completed on March 22, 2023

        decomposed = {}
        st = strs[0] #ideally would be better to choose the shortest elem in List strs
        max_prefix_i = len(st)

        for i in range(len(st)+1):
            decomposed[st[0:i]] = i

        prefix_i = max_prefix_i

        # loop through each element in List O(N)
        for i in range(1,len(strs)):
            # length of current element
            len_curr = len(strs[i])
            # max prefix would be as long as str. do not want to error if curr elem is shorter
            d = min(prefix_i,len_curr)

            while d >= 0:
                # look at substring of element from 0 to max prefix
                sub_st = strs[i][0:d]
                if sub_st in decomposed:
                    # determine lowest common prefix number
                    prefix_i = min(decomposed[sub_st],prefix_i)
                    break # do not need to continue if found
                elif d == 0:
                    return "" # if no match, then can end function
                else: #keep looking at smaller prefixes in element
                    d -= 1

        return st[0:prefix_i]
