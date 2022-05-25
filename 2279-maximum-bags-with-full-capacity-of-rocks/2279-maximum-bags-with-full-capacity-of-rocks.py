class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        ans=0
      
        for i in range(len(rocks)):
            rocks[i]=capacity[i]-rocks[i]
            
        rocks.sort()
        for i in range(len(rocks)):
            if rocks[i]<=additionalRocks:
                additionalRocks-=rocks[i]
                
                ans+=1
        
        
                
        return ans
        