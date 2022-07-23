class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
            
        rows = len(matrix) 
        cols = len(matrix[0])
        
        up = left = 0
        down = rows- 1
        right = cols - 1
        
        while len(res) < rows * cols:
            
            for c in range(left, right+1):
                res.append(matrix[up][c])
                print(matrix[up][c])
            
            for r in range(up+1, down+1):
                res.append(matrix[r][right])
            
            #making sure we are not on the same row 
            if up != down:
                #traverse from right to left
                for c in range(right-1 , left-1, -1):
                    res.append(matrix[down][c])
                
            if right != left:
                for r in range(down-1 , up , -1):
                    res.append(matrix[r][left])
                    
            left +=1
            right -=1
            up +=1
            down -=1
            
        return res