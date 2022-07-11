class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#         ans=0
#         for i in range(len(nums)):
#             ans^=nums[i]
            
#         return ans;
        h=collections.defaultdict(int)
        for i in range(len(nums)):
            h[nums[i]]+=1
            
        for key,value in h.items():
            if value>1:
                return key
        # print(h)
        