class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        
        
        def getans(n, m, s, t, dp):
            
            if m<0:
                return 1
            
            if n<0:
                return 0
            
            if dp[n][m]!=-1:
                return dp[n][m]
            
            if s[n]==t[m]:
                dp[n][m] = getans(n-1, m-1, s, t, dp) + getans(n-1, m, s, t, dp)
                return dp[n][m]
            
            dp[n][m] = getans(n-1, m, s, t, dp)
            
            return dp[n][m]
        
        
        
        
        
        
        
        dp=[]
        
        n=len(s)
        m=len(t)
        for i in range(n):
            x=[]
            for j in range(m):
                x.append(-1)
            dp.append(x)
        return getans(n-1, m-1, s, t, dp)
        
        