class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=len(nums)
        if nums[l-1]<target:
            return l
        for i in range(0,l):
            if nums[i]==target:
                return i
            elif nums[i]>target:
                return i