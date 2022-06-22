class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum =[0] * len(nums)
        right_sum=[0] * len(nums)
        
        for i in range(1,len(nums)):
            left_sum[i] = left_sum[i-1] + nums[i-1]
            
        
        for j in range(len(nums)-2,-1,-1):
            right_sum[j] = right_sum[j+1] + nums[j+1]
        print(right_sum)
            
        for j in range(len(nums)):
            if left_sum[j] == right_sum[j]:
                return j
        return -1