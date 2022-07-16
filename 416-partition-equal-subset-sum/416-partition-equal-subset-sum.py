class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        
        def getans(nums, t, i, dp):
            if i>=len(nums) or t<0:
                return False
            if t==0:
                return True
            
            if dp[i][t]!=-1:
                return dp[i][t]
            
            dp[i][t] = getans(nums, t, i+1, dp) or getans(nums, t-nums[i], i+1, dp)
            
            return dp[i][t]
        
        
        
        
        total = 0
        for i in nums:
            total+=i
            
        dp=[]
        for i in range(len(nums)):
            x=[]
            for j in range(total//2 + 1):
                x.append(-1)
            dp.append(x)
        
        
        if total%2!=0:
            return False
        else:
            return getans(nums, total//2, 0, dp)
        