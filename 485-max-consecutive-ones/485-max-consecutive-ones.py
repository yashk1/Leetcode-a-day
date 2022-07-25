class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        curr_max = 0 
        for i in nums:
            if i == 1:
                curr_max +=1 
                maxx = max(maxx, curr_max)
            else:
                curr_max = 0
        return maxx