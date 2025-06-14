class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        t=[]
        s=s.split()
        for i in range(0,len(s)):
            if i<k:
                t.append(s[i])
        return ' '.join(t)
                
        