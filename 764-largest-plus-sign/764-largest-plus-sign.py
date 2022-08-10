class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        left=[]
        right=[]
        up=[]
        down=[]
        arr=[]
        for i in range(n):
            x=[]
            for j in range(n):
                x.append(1)
            arr.append(x)
            
        for i in range(n):
            x=[]
            for j in range(n):
                x.append(0)
            left.append(x)
        
        for i in range(n):
            x=[]
            for j in range(n):
                x.append(0)
            right.append(x)
        for i in range(n):
            x=[]
            for j in range(n):
                x.append(0)
            up.append(x)
        for i in range(n):
            x=[]
            for j in range(n):
                x.append(0)
            down.append(x)
            
        for i in mines:
            x=i[0]
            y=i[1]
            arr[x][y]=0
            
        for i in range(n):
            left[i][0]=arr[i][0]
            for j in range(1, n):
                if arr[i][j]!=1:
                    left[i][j]=0
                else:
                    left[i][j]=1+left[i][j-1]
                    
        for i in range(n):
            right[i][n-1]=arr[i][n-1]
            for j in range(n-2, -1, -1):
                if arr[i][j]!=1:
                    right[i][j]=0
                else:
                    right[i][j]=1+right[i][j+1]
                    
        for i in range(n):
            up[0][i]=arr[0][i]
            for j in range(n):
                if arr[i][j]!=1:
                    up[i][j]=0
                else:
                    up[i][j]=1+up[i-1][j]
                    
        for i in range(n):
            down[n-1][i]=arr[n-1][i]
            for j in range(n-2, -1, -1):
                if arr[j][i]!=1:
                    down[j][i]=0
                else:
                    down[j][i]=1+down[j+1][i]
                    
        ans=float("-inf")
        for i in range(n):
            for j in range(n):
                val = min(up[i][j], down[i][j], left[i][j], right[i][j])
                
                ans=max(ans, val)
                
        return ans
                    

        