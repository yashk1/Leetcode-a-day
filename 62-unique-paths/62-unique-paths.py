class Solution(object):
    def uniquePaths(self, m, n):
        if m==0 or n==0:
            return 0 
        if n == 1 or m==1:
            return 1 
        
        
        matrix = [[1 for i in range(n)] for j in range(m)]
        print(matrix)
        
        for col in range(1, m):
            for row in range(1,n):
                matrix[col][row] = matrix[col-1][row] + matrix[col][row-1]
        return matrix[-1][-1]