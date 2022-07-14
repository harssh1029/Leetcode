class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        
        def getans(m, n, obstacleGrid, dp):
            if (m>=0 and n>=0) and obstacleGrid[m][n]==1:
                return 0
            
            if m==0 and n==0:
                return 1
            if m<0 or n<0:
                return 0
            
            if dp[m][n]!=0:
                return dp[m][n]
            
            up=getans(m-1,n, obstacleGrid, dp)
            left=getans(m, n-1, obstacleGrid, dp)
            dp[m][n]=up+left
            return dp[m][n]
            
        
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[]
        for i in range(m+1):
            x=[]
            for j in range(n+1):
                x.append(0)
                
            dp.append(x)
            
        if m==1 and n==1:
            if obstacleGrid[0][0]==0:
                return 1
            else:
                return 0
        
        
            
            
        getans(m-1, n-1, obstacleGrid, dp)
        return dp[m-1][n-1]