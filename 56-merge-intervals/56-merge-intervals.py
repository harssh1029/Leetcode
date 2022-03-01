class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        leng = len(intervals)
        ans=[]
        intervals.sort()
        j=0
        ans.append(intervals[0])
        for i in range(1, leng):
            if(ans[j][1]>=intervals[i][0]):
                ans[j][1]=max(ans[j][1], intervals[i][1])
            else:
                ans.append(intervals[i])
                j+=1
                
        return ans