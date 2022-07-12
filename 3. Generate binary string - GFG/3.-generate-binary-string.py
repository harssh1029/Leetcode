#User function Template for python3


class Solution:
    def generate_binary_string(self,s):
        # Code here
        
        def getans(idx, arr, ans):
            if idx==len(arr):
                val=""
                
                for i in arr:
                    val+=i
                # print(val)
                ans.append(val)
                return
                
            
            if arr[idx]=="?":
                #x="0"
                for ch in "01":
                    arr[idx]=ch
                    getans(idx+1, arr, ans)
                    arr[idx]="?"
                    
            else:
                getans(idx+1, arr, ans)
                        
        
        ans=[]
        arr=list(s)
        getans(0, arr, ans)
        return ans
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		s= input()
		ob = Solution()
		ans = ob.generate_binary_string(s)
		for i in ans:
		    print(i, end = " ")
		print()
# } Driver Code Ends