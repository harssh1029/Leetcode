class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n=len(nums)
        dp1=[1]*n
        dp2=[1]*n
        ans=0
        for i in range(0, n):
            for j in range(0, i):
                if nums[i]>nums[j] and 1+dp1[j]>dp1[i]:
                    dp1[i]=1+dp1[j]
                    
        for i in range(n-1, -1, -1):
            for j in range(n-1, i, -1):
                if nums[i]>nums[j] and 1+dp2[j]>dp2[i]:
                    dp2[i]=1+dp2[j]
        
            if dp1[i]>1 and dp2[i]>1:
                ans=max(ans, dp1[i]+dp2[i]-1)
        
        
#         for i in range(n):
#             ans=max(ans, dp1[i]+dp2[i]-1)
        
        return n-ans
                
        
        