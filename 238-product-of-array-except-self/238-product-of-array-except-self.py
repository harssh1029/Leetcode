class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalproduct = 1
        for i in range(len(nums)):
            totalproduct*=nums[i]
            
        withoutzero=1
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            else:
                withoutzero*=nums[i]
        
        ans=[]
        if nums.count(0)==len(nums):
            ans=[0]*len(nums)
            return ans
        elif nums.count(0)==1:
            for i in range(len(nums)):
                if nums[i]==0:
                    ans.append(withoutzero)
                else:
                    ans.append(0)
            
        elif nums.count(0)>1:
            ans=[0]*len(nums)
            return ans
        else:
            for i in range(len(nums)):
                ans.append(totalproduct//nums[i])
                
        return ans