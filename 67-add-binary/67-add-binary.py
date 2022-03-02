class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans=""
        a, b = a[::-1], b[::-1]
        carry=0
    
        for i in range(max(len(a), len(b))):
            chara = ord(a[i])-ord("0") if i<len(a) else 0
            charb = ord(b[i])-ord("0") if i<len(b) else 0
            sumdigit = (chara + charb + carry) %2
            ans=str(sumdigit)+ans
            
            carry = (chara + charb + carry) // 2
            
            
        if carry!=0:
            ans="1"+ans
        
        return ans
            
            