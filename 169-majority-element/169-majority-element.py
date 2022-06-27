class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h=collections.defaultdict(int)
        for i in range(len(nums)):
            h[nums[i]]+=1
            
        maxiele = float("-inf")
        for i in h.keys():
            if h[i] > (len(nums)//2):
                maxiele = max(maxiele, i)
                
        return maxiele