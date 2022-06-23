class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        subsets = self.subsets(nums[:-1])
        new = [subset + [nums[-1]] for subset in subsets]
        return subsets + new