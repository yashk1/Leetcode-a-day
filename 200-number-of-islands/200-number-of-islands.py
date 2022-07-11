class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid,i,j)
                    count+=1
        return count
    
    def dfs(self, grid, i , j):
        
        R ,C = len(grid), len(grid[0])
        
        if i < 0 or i >= R or j < 0 or j >= C or grid[i][j] != '1':
            return 
        
        grid[i][j] = '#' #all the visted pixels are changed to #
        
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        
#time - O(MxN)
#space - O(MxN)in case that the grid map is filled with lands where DFS goes M×N deep.

