class Solution:
    def maxAscendingSum(self, nums):
        current_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                max_sum = max(max_sum, current_sum)
                current_sum = nums[i]
        max_sum = max(max_sum, current_sum)
        return max_sum
