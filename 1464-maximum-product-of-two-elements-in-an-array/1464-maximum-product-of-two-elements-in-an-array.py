class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        max=nums[0]
        max1=nums[1]
        res=(max-1)*(max1-1)
        return res
        
        