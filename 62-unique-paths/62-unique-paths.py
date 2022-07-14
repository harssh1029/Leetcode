class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        def getans(m, n, dp):
            if m==0 and n==0:
                return 1
            if m<0 or n<0:
                return 0
            if dp[m][n]!=-1:
                return dp[m][n]
            
            up=getans(m-1, n, dp)
            left=getans(m, n-1, dp)
            dp[m][n]=up+left
            return dp[m][n]
        
        
        
        
        
        dp=[]
        for i in range(m+1):
            x=[]
            for j in range(n+1):
                x.append(-1)
            dp.append(x)
            
        if m==1 and n==1:
            return 1
                
        getans(m-1, n-1, dp)
        # print(dp)
        return dp[m-1][n-1]
        