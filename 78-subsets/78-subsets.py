class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets=[[]]
        for ele in nums:
            for i in range(len(subsets)):
                s = subsets[i]
                subsets.append(s+[ele])
                
        return subsets
        