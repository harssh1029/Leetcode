class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        visited = set()
        ans = 0
        
        for num in nums:
            if num-1 in hashset:
                continue
                
            if num-1 in visited:
                continue
                
            currentlen = 0
            visited.add(num)
            while num+currentlen in hashset:
                currentlen+=1
                
            
            ans = max(ans, currentlen)
            
        return ans
        