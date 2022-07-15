class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        dict = {}
        
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        if n-1 not in dict: dict[n-1] = self.climbStairs(n-1)
        if n-2 not in dict: dict[n-2] = self.climbStairs(n-2)
            
        return dict[n-1] + dict [n-2]