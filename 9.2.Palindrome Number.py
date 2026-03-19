class Solution(object):
    def isPalindrome(self, x):
        if x<0 or (x%10 == 0 and x!= 0):
            return False
        
        t = x
        rev = 0
        while t > rev:
            rev = rev*10 + t%10
            t = t//10

        return t==rev or t == rev//10