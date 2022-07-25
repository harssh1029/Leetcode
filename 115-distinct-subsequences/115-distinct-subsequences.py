class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        
        
#         def getans(n, m, s, t, dp):
            
#             if m<0:
#                 return 1
            
#             if n<0:
#                 return 0
            
#             if dp[n][m]!=-1:
#                 return dp[n][m]
            
            
            
#             return dp[n][m]
        
        
        
        
        
        
        
        dp=[]
        
        n=len(s)
        m=len(t)
        for i in range(n+1):
            x=[]
            for j in range(m+1):
                x.append(0)
            dp.append(x)
            
        for i in range(n+1):
            dp[i][0]=1
            
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][m]
        
        