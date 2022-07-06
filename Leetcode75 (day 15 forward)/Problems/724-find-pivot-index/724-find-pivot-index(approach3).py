class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        
        left_sum = 0
        
        
        for i in range(len(nums)):
            if left_sum == (total_sum - nums[i] - left_sum):
                return i
            left_sum += nums[i]
        return -1

#this approach is the best. Cuz we can eaisly loop through the aray from left to right and calculate left_sum and to calculate right_summ all we have to do is subtract left_sum + current element from total sum