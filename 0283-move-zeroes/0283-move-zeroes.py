class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        #find the first occurance of zero
        
        k = 0
        while k < len(nums):
            if nums[k] == 0:
                break
            else:
                k+=1
                
        
        i = k
        j = k+1 #set two pointer at k and k+1 i.e first occurance of zero and next element
        
        while j < len(nums):
            if nums[j] !=0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j+=1
            else:
                j+=1
        return nums