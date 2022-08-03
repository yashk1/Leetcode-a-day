class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        
        ls = 0
        
        for i in range(len(nums)):
            if ls == (total_sum - nums[i] - ls):
                return i
            ls = ls + nums[i]
        return -1