class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        def getans(m, n, matrix, dp):
            
            if n<0 or n>=len(matrix[0]):
                return float("inf")
            
            if m==0:
                return matrix[m][n]
            
            if dp[m][n]!=-1:
                return dp[m][n]
            
            up=matrix[m][n]+getans(m-1, n, matrix, dp)
            leftd = matrix[m][n]+getans(m-1, n-1, matrix, dp)
            rightd = matrix[m][n] + getans(m-1, n+1, matrix, dp)
            dp[m][n]=min(up, min(leftd, rightd))
            
            return dp[m][n]
        
        
        dp=[]
        
        m=len(matrix)
        n=len(matrix[0])
        ans=float("inf")
        
        for i in range(m):
            x=[]
            for j in range(n):
                x.append(-1)
            dp.append(x)
        
        for i in range(n):
            ans=min(ans, getans(m-1,i, matrix, dp))
            
        return ans
        