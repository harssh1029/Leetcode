class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp=[]
        n=len(str1)
        m=len(str2)
        for i in range(n+1):
            x=[]
            for j in range(m+1):
                x.append(0)
            dp.append(x)
            
        h=collections.defaultdict(int)
        for i in range(1, n+1):
            for j in range(1, m+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                    
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])
            
        
        leng=dp[n][m]
        i=n
        j=m
        ans=""
        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                ans+=str1[i-1]
                i-=1
                j-=1
            elif dp[i-1][j]>dp[i][j-1]:
                ans+=str1[i-1]
                i-=1
            else:
                ans+=str2[j-1]
                j-=1
                
        while i>0:
            ans+=str1[i-1]
            i-=1
        while j>0:
            ans+=str2[j-1]
            j-=1
            
        return ans[::-1]