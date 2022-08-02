class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = 0 
        
        for right in range(len(nums)):
            if nums[right] != val:
                nums[curr] = nums[right]
                curr+=1
        return curr 
        
     
        
        