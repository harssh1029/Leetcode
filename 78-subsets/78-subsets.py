class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(start, curr_list):
            ans.append(curr_list[:])
            
            for j in range(start, n):
                curr_list.append(nums[j])
                backtrack(j+1, curr_list)
                curr_list.pop()
        
        
        n=len(nums)
        ans=[]
        backtrack(0, [])
        return ans
        