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
            dp[n]=max(take, nottake)
            return dp[n]
        
        
        
        if len(nums)==1:
            return nums[0]
        
        if len(nums)==2:
            return max(nums[0], nums[1])
        dp1 = [-1]*len(nums)
        dp2= [-1]*len(nums)
        firstremove=nums[1:]
        lastremove=nums[:-1]
        getans(len(firstremove)-1, nums[1:], dp1)
        getans(len(lastremove)-1, nums[:-1], dp2)
        
        return max(dp1[len(firstremove)-1], dp2[len(lastremove)-1])
        