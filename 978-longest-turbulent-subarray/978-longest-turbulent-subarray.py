class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        
        def getans(n, arr, sign, ans, leng):
            for i in range(n-1):
                if arr[i]<arr[i+1]:
                    if sign==1:
                        leng+=1
                    else:
                        leng=0
                elif arr[i]>arr[i+1]:
                    if sign==-1:
                        leng+=1
                    else:
                        leng=0
                else:
                    leng=0
                        
                sign*=-1
                ans=max(ans, leng)
            return ans
        
        
        
        n=len(arr)
        if n==1:
            return 1
        
        #<
        ans1 = getans(n, arr, 1, 0, 0)
        ans2= getans(n, arr , -1, 0, 0)
        return max(ans1, ans2)+1
        