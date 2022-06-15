# this code will give runtime beacuse it exceeds the time limit
# to solve it more efficiently we need to using dynamic programming or memoization
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 1 or m ==1:
            return 1    
            # there can be only one path if the matrix is 1d
        else:
            return self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)