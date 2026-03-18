class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(l,r):
            while l>=0 and r< len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1: r]
        
        res = ""
        for i in range(len(s)):
            # odd
            odd = expand(i,i)

            # even
            even = expand(i, i+1)

            if len(res) < len(odd):
                res = odd

            if len(res) < len(even):
                res = even
        return res