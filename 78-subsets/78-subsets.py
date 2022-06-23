class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        op = [[]]
        
        for number in nums:
            op = op + [cur + [number] for cur in op]
        return op