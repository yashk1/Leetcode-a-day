class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        
        if len(nums) <1: return 0 
        curr = 0 

        for right in range(1, len(nums)):
            if nums[curr] != nums[right]:
                curr +=1 #main part is this. when we have encountered all the duplicates the curr will increment
                nums[curr] = nums[right]
        return curr+1