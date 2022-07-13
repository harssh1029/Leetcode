#User function Template for python3

class Solution:
    def AllParenthesis(self,n):
        #code here
        
        def getans(open, close, ans, n, s):
            if open==n and close==n:
                ans.append(s)
                return 
            
            if open<n:
                getans(open+1, close, ans, n, s+"(")
                
            if close<open:
                getans(open, close+1, ans, n, s+")")
        
        
        
        ans=[]
        s=""
        getans(0, 0, ans, n, s)
        return ans
        
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3


        
if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        ob=Solution()
        result=ob.AllParenthesis(n)
        result.sort()
        for i in range(0,len(result)):
            print(result[i])
        

# } Driver Code Ends