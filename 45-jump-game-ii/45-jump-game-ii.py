class Solution:
    def jump(self, nums: List[int]) -> int:
        
        
        
#         def getans(idx, nums, n, dp):
#             if idx==n:
#                 return 0
            
#             if idx>n:
#                 return float("inf")
            
#             if dp[idx]!=-1:
#                 return dp[idx]
            
#             steps=float("inf")
#             for i in range(1, nums[idx]+1):
#                 steps = min(steps, 1+getans(idx+i, nums, n, dp))
                
#             dp[idx]=steps
#             return dp[idx]
        
        
#         n=len(nums)
#         dp=[-1]*len(nums)
#         return getans(0, nums, n-1, dp)

        n=len(nums)
        dp=[0]*n
        
        for i in range(n-2, -1, -1):
            temp=float("inf")
            for j in range(1, nums[i]+1):
                if i+j < n:
                    temp = min(temp, 1+dp[i+j])
                
            dp[i]=temp
                
        return dp[0]
        