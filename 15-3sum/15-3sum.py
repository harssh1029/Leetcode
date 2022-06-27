class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #-4 -1 -1 0 1 2 
        nums.sort()
        ans=set()
        for i in range(len(nums)-2):
            start=i+1
            end=len(nums)-1
            while start<end:
                x=(nums[start]+nums[end]+nums[i])
                if (x==0):
                    ans.add((nums[i], nums[start], nums[end]))
                    start+=1
                    end-=1
                elif x<0:
                    start+=1
                else:
                    end-=1
                
                
        return ans
        