class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        #using two pointer
        
        n=len(nums)
        
        result = [0] * n
        
        left = 0
        
        right = n-1
        
        for i in range(n-1, -1, -1): #looping from back bcz array is sorted
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -=1
            else:
                square = nums[left]
                left += 1
            
            result[i] = square * square
            
        return result


#time - O(N)
#space- O(1) not accounting for output array