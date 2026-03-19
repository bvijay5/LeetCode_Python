class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        l = 0
        res = 0

        for r, el in enumerate(s):
            if el in seen and seen[el]>=l:
                l = seen[el]+1
            seen[el] = r
            res = max(res, r-l+1)
        return res