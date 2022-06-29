class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=[]
        n=1
        for i in range(0, rowIndex+1):
            ans.append(n)
            n=n*(rowIndex-i)//(i+1);
            
        return ans
        