class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        def getans(n, nums, dp):
            if n==0:
                return nums[n]
            if n<0:
                return 0
            if dp[n]!=-1:
                return dp[n]
            take = nums[n]+getans(n-2, nums, dp)
            nottake = 0 + getans(n-1, nums, dp)
            
            dp[n] = max(take, nottake)
            return dp[n]        
        
        
        if len(nums)==1:
            return nums[0]
        dp=[-1]*len(nums)
        getans(len(nums)-1, nums, dp)
        return dp[len(nums)-1]
        