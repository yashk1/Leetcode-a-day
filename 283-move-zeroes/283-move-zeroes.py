class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        if len(nums) <= 1:
            return nums
        
        curr = 0 
        for i in range(len(nums)):
            if nums[i] !=0:
                nums[curr] , nums[i] = nums[i], nums[curr]
                curr+=1
                
        return nums
                
