class Solution:
    def majorityElement(self, nums: List[int]) -> int:
#         h=collections.defaultdict(int)
#         for i in range(len(nums)):
#             h[nums[i]]+=1
            
#         maxiele = float("-inf")
#         for i in h.keys():
#             if h[i] > (len(nums)//2):
#                 maxiele = max(maxiele, i)
                
#         return maxiele
        count=1
        n=len(nums)
        val=nums[0]
        for i in range(1, n):
            if nums[i]==val:
                count+=1
            else:
                count-=1
                
            if count<0:
                val=nums[i]
                count=1
                
        return val