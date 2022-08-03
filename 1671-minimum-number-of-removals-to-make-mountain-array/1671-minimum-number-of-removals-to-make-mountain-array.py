class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n=len(nums)
        dp1=[1]*n
        dp2=[1]*n
        ans=0
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j] and dp1[i]<1+dp1[j]:
                    dp1[i]=dp1[j]+1
                    
                    
        for i in range(n-1, -1, -1):
            for j in range(n-1, i, -1):
                if nums[i]>nums[j] and dp2[i]<1+dp2[j]:
                    dp2[i]=dp2[j]+1
                    
            if dp1[i]>1 and dp2[i]>1:
                ans=max(ans, dp1[i]+dp2[i]-1)
        
        return n-ans
                
        
        