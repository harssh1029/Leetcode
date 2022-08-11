class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dp=[1]*n
        h=collections.defaultdict(int)
        maxi=1
        lastidx=0
        nums.sort()
        for i in range(n):
            h[i]=i
            for j in range(0, i):
                if nums[i]%nums[j]==0 and 1+dp[j]>dp[i]:
                    dp[i]=1+dp[j]
                    h[i]=j
                    
            if dp[i]>maxi:
                maxi=dp[i]
                lastidx=i
                
        ans=[]
        ans.append(nums[lastidx])
        while h[lastidx]!=lastidx:
            lastidx = h[lastidx]
            ans.append(nums[lastidx])
            
        return ans[::-1]
                    
        