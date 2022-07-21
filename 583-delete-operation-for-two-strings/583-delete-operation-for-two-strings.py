class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[]
        for i in range(len(word1)+1):
            x=[]
            for j in range(len(word2)+1):
                x.append(-1)
            dp.append(x)
            
        for i in range(len(word1)+1):
            dp[i][0]=0
            
        for i in range(len(word2)+1):
            dp[0][i]=0
            
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])
                    
        #print(dp[len(word1)][len(word2)])
                    
        return (len(word1)+len(word2))-2*dp[len(word1)][len(word2)]
        