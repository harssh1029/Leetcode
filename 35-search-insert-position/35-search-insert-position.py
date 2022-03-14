class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        mid=int(start+(end-start)/2)
        if(target > nums[end]):
            return len(nums)
         
        while(start<end):
            if(nums[mid] == target):
                return mid
            
            if(nums[mid] < target):
                start = mid + 1
            
            else:
                end = mid;
            mid = int(start + (end-start)/2)
            
        return mid