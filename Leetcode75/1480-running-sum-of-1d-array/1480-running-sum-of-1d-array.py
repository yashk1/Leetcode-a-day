class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

#complexity of this function is O(n) as the for loop will run for the lenght of nums array
#Time complexity - O(n)
#Space complexity  - O(1)