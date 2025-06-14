class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=[]
        t=[]
        for i in nums:
            s.append(i*i)
        s=sorted(s)
        return s

        