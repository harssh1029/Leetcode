class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        def getans(s, i, dp):
            if i==len(s):
                return 1
            
            if s[i]=="0":
                return 0
            
            if dp[i]!=-1:
                return dp[i]
            
            nottake = take = 0
            nottake = getans(s, i+1, dp)
            if int(s[i:i+2]) < 27 and i!=len(s)-1:
                take = getans(s, i+2, dp)
                
            dp[i]=take+nottake
            return dp[i]
        
        
        
        
        
        
        dp=[-1]*(len(s)+10)
        return getans(s, 0, dp)
        