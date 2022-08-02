class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        c= 0 
        
        for r in range( len(nums)):
            if nums[r] %2 ==0:
                nums[r], nums[c] = nums[c], nums[r]
                c+=1
        return nums