class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        
        def helper(index, arr, temp=[]):
            ans.append(temp.copy())
            for i in range(index, len(arr)):
                if i!=index and arr[i]==arr[i-1]:
                    continue
                    
                temp.append(arr[i])
                helper(i+1, arr, temp)
                temp.pop()
         
        helper(0, nums)
        return ans