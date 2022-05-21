#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        dictans = {}
        ansmax = 0
        currentsum = 0
        
        for i in range(len(arr)):
            currentsum += arr[i]
            if currentsum == 0:
                ansmax = i+1
                
            else:
                if currentsum in dictans:
                    ansmax = max(ansmax, i-dictans[currentsum])
                else:
                    dictans[currentsum]=i
                    
        return ansmax

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends