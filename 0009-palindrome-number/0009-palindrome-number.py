class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        t1=str(x)
        t=t1[::-1]
        if t==t1:
            return True
        else:
            return False
        