class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        s=len(nums)
        for i in range(start,len(nums)):
            if(nums[i]==target):
                s=min(s,abs(start-i))
        return s

        