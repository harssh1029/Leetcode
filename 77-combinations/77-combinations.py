class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def getans(i, temp):
            if len(temp)==k:
                ans.append(temp.copy())
                return
            
            for i in range(i,n+1):
                temp.append(i)
                getans(i+1, temp)
                temp.pop()
                
        getans(1, [])
        return ans
        
#         def getans(1,ans, temp):
#             if len(temp)==k:
#                 ans.append(temp.copy())
#                 return
            
#             for i in range(1, n+1):
#                 temp.append(i)
#                 getans(n, k, i+1, ans, temp)
#                 temp.pop()
        
#         getans(1, ans, [])
#         return ans
        
    
        
        
        
        