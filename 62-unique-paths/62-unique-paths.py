class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        rows, cols = m, n
        
        path_dp = [ [ 1 for j in range(cols)] for i in range(rows) ]
        
        
        # Dynamic Programming relation:
        
        # Base case:
        # DP(0, j) = 1 , only reachable from one step left
        # DP(i, 0) = 1 , only reachable from one step up
        
        # General case:
        # DP(i,j) = number of path reach to (i, j)
        #         = number of path reach to one step left + number of path reach to one step up
        #         = number of path reach to (i, j-1) + number of path to (i-1, j)
        #         = DP(i, j-1) + DP(i-1, j)
        
        
        
        for i in range(1, rows):
            for j in range(1, cols):
                
                path_dp[i][j] = path_dp[i][j-1] + path_dp[i-1][j]
        
        
        # Destination coordination = (rows-1, cols-1)
        return path_dp[rows-1][cols-1]