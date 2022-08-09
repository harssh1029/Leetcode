class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        if len(arr)==1:
            return arr[0]
        
        n=len(arr)
        allnegative = True
        
        count=0
        for i in arr:
            if i<0:
                count+=1 
                
            
        if count==n:
            return max(arr)
        
        forward = [0]*len(arr)
        curr1=0
        forward.append(arr[0])
        for i in range(0, len(arr)):
            curr1 +=arr[i]
            if curr1<0:
                curr1=0
            
            forward[i]=curr1
            
        backward=[0]*len(arr)
        curr2=0
        backward.append(arr[n-1])
        for i in range(len(arr)-1, -1, -1):
            curr2 += arr[i]
            if curr2<0:
                curr2=0
            backward[i]=curr2
            
        ans=float("-inf")
        for i in range(n-2):
            ans=max(ans, max(forward[i], forward[i]+backward[i+2]))
            
        print(forward)
        print(backward)
            
        ans=max(ans, max(forward[n-1], forward[n-2]))
        
        return ans