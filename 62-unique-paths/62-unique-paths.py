class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        def getans(m, n,dp):
            
            if m==0 and n==0:
                return 1
            
            if m<0 or n<0:
                return 0
            
            if dp[m][n]!=-1:
                return dp[m][n]
            
            up=getans(m-1, n, dp)
            left=getans(m, n-1, dp)
            dp[m][n]=left+up
            
            return dp[m][n]
            
            
            
        
        
        dp=[]
        for i in range(m):
            x=[]
            for j in range(n):
                x.append(-1)
            dp.append(x)
            
        
        return getans(m-1, n-1, dp)
        