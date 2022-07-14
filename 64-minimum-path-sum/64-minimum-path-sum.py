class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        def getans(m, n, grid, dp):
            if m==0 and n==0:
                return grid[m][n]
            if m<0 or n<0:
                return float("inf")
            if dp[m][n]!=0:
                return dp[m][n]
            
            up = grid[m][n]+getans(m-1, n, grid, dp)
            left = grid[m][n]+getans(m, n-1, grid, dp)
            dp[m][n]=min(up, left)
            return dp[m][n]
        
        
        dp=[]
        
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            x=[]
            for j in range(n):
                x.append(0)
            dp.append(x)
                
        return getans(m-1, n-1, grid, dp)
        