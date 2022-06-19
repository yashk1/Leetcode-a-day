class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = [i for i in range(1, n+1)]
        
        
        while len(circle)  >1:
            i = (k-1) % len(circle)
            circle.pop(i)
            circle = circle[i:]+circle[:i]
            
        return circle[0]