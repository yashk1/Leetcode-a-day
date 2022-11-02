class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        #create a new array 
        n = len(nums)
        
        res = [0] * n
        
        for i in range(n):
            res[(i+k) % n] = nums[i] 
            # %n is used to solve the case where we rotate by let's say 404.
            #technically it is only rotating by 4 and also rotating 
            
        nums[:] = res
        
        