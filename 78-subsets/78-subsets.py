class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        for i in nums:
            for j in range(len(ans)):
                s = ans[j]
                ans.append(s+[i])
            
        return ans
        