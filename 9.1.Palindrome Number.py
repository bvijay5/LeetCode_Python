class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        t = x
        res = 0
        while t != 0:
            res = res*10 + t%10
            t = t//10
            
        return res == x