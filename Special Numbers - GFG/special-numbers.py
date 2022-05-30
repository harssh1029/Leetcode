#User function Template for python3

class Solution:
    def getSpecialNumber(self, n):
        # code here 
        ans=str()
        n-=1
        while n:
            ans+=str(n%6)
            n//=6
            
        return ans[::-1] if ans else 0
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.getSpecialNumber(n))
# } Driver Code Ends