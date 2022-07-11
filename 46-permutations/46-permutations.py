class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def getans(idx, nums, ans):
            if idx==len(nums)-1:
                ans.append(nums[:])
                
            else:
                for j in range(idx, len(nums)):
                    nums[idx], nums[j] = nums[j], nums[idx]
                    getans(idx+1, nums, ans)
                    nums[idx], nums[j] = nums[j], nums[idx]
                    
        
        ans=[]
        getans(0, nums, ans)
        return ans
    