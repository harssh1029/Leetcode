class Solution:
    def minInsertions(self, s: str) -> int:
        
        
        def getans(s1, s2, dp):
            for i in range(len(s1)+1):
                dp[i][0]=0
                dp[0][i]=0
                
            for i in range(1,len(s1)+1):
                for j in range(1, len(s1)+1):
                    if s1[i-1]==s2[j-1]:
                        dp[i][j]=1+dp[i-1][j-1]
                    else:
                        dp[i][j]=max(dp[i-1][j], dp[i][j-1])
                        
            return dp[len(s)][len(s)]
        
        
        
        
        
        
        
        
        dp=[]
        for i in range(len(s)+1):
            x=[]
            for j in range(len(s)+1):
                x.append(-1)
            dp.append(x)
            
        s2=s[::-1]
        return (len(s)-getans(s,s2,dp))