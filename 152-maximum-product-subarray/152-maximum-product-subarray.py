class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res=max(nums)
        
        currmax, currmin = 1, 1
        
        for i in range(len(nums)):
            
            
            temp = nums[i]*currmax
            currmax = max(nums[i]*currmax, nums[i]*currmin, nums[i])
            currmin = min(temp, nums[i]*currmin, nums[i])
            
            res = max(res, currmax)
            
        return res