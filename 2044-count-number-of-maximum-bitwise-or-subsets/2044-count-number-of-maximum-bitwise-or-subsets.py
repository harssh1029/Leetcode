class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxi=0
        for i in range(len(nums)):
            maxi|=nums[i]
            
        count=0
        totalsubset = pow(2, len(nums))
        for i in range(totalsubset):
            orr=0
            for j in range(len(nums)):
                if (i&(1<<j)):
                    orr|=nums[j]
                    
            if orr==maxi:
                count+=1
        
        return count