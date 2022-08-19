class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        start=0
        maxlen=1
        for i in range(1, len(s)):
            #even
            l=i-1
            r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > maxlen:
                    maxlen = r-l+1
                    start=l
                l-=1
                r+=1
                
            #odd
            l=i-1
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > maxlen:
                    maxlen = r-l+1
                    start=l
                r+=1
                l-=1
                
            
        return s[start:start+maxlen]
            