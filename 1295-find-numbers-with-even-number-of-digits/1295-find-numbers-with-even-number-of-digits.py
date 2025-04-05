class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            d=str(i)
            if len(d)%2==0:
                c=c+1
        return c
        