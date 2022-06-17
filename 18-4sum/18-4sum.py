class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # Write your code here.-1 1 2 4 6 7
        nums.sort()
        ans=set()
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                first = j+1
                end=len(nums)-1
                
                while first<end:
                    curr = nums[i]+nums[j]+nums[first]+nums[end]
                    
                    if curr==target:
                        # x=[nums[i],nums[j],nums[first],nums[end]]
                        # if x not in ans:
                        ans.add((nums[i],nums[j],nums[first],nums[end]))
                        # #print(curr)
                        first+=1
                        end-=1
                    elif curr>target:
                        end-=1
                    else:
                        first+=1
    
        return ans
                    

        