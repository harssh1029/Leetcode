class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp=[]
        for i in range(len(text1)+1):
            x=[]
            for i in range(len(text2)+1):
                x.append(0)
            dp.append(x)
        
        for i in range(len(text1)+1):
                dp[i][0]=0
        for i in range(len(text2)+1):
                dp[0][i]=0
                
            
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])
                    
        return dp[len(text1)][len(text2)]
        