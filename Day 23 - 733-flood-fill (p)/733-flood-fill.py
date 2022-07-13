class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newcolor: int) -> List[List[int]]:
        #change the adjacent pixel that have the same color as starting pixel
        R, C = len(image), len(image[0])
        color = image[sr][sc] #old color 
        
        
        def dfs(i, j):
            
            if i < 0 or i>= R or j< 0 or j>= C:  
                return
            if image[i][j] != color or image[i][j] == newcolor: 
            #case when the adjacent pixel doesnt have the same color as starting pixel or adjacent pixel is already of the new color, no change
                return
            
            image[i][j] = newcolor #
            
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        dfs(sr,sc)
        return image
        
#time complexity - O(n) #worst case we change the color of all the pixels adjacent
#space complexity - O(n) #the size of the implicit call stack when calling dfs.

 