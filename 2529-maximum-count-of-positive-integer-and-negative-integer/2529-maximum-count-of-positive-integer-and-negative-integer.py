class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        c=0
        c1=0
        for i in nums:
            if i>0:
                c=c+1
            elif i<0:
                c1=c1+1
        if c>c1:
            return c
        else:
            return c1
        