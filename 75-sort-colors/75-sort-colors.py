class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countzero = nums.count(0)
        countsecond = nums.count(2)
        start=0
        end=len(nums)-1
        while countzero>0 or countsecond>0:
            if countzero>0:
                if nums[start]!=0:
                    nums[start]=0
                countzero-=1
                start+=1
                    
            if countsecond>0:
                if nums[end]!=2:
                    nums[end]=2
                countsecond-=1
                end-=1
                    
        for i in range(start, end+1):
            nums[i]=1
            
        return nums
        
        
                
                    
            
                    
                
        