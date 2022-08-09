class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        
        def getans(prefsum, target):
            h=collections.defaultdict(int)
            h[0]=1
            summ=0
            ans=0
            for i in range(len(prefsum)):
                summ+=prefsum[i]
                ans+=h[summ-target]
                h[summ]+=1
                
            return ans
            
        
        
        
        
        count=0
        for i in range(len(matrix)):
            prefsum=[0]*len(matrix[i])
            for j in range(i, len(matrix)):
                for k in range(len(matrix[j])):
                    prefsum[k]+=matrix[j][k]
                    
                count+=getans(prefsum, target)
                
                
        return count
        