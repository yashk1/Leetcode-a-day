# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        
        while left < right:
            mid = left + (right-left) //2
            
            if (isBadVersion(mid)): #in this we cant compare like regular binary search with elements we have to see the true value untill we find the first one
                right = mid
            else:
                left = mid +1
        return left #or left doesnt matter loop will exit wehn l==r
                