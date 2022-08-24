class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = max_subarray = nums[0]
        
        for num in nums[1:]:
            current_subarray = max(num, num+current_subarray)
            max_subarray = max(max_subarray, current_subarray)
            
        return max_subarray
            
        
        
        