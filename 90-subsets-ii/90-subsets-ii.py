class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for element in nums:
            for i in range(len(subsets)):
                s = subsets[i]
                x = [element]+s
                x.sort()
                subsets.append(x)
                
        ans = []
        for i in subsets:
            i.sort()
            if i not in ans:
                ans.append(i)
                
        return ans
        