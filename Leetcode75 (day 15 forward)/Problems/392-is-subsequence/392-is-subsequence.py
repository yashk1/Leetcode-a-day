class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = right = 0
        n=len(s)
        m=len(t)
        
        while left < n and right < m:
            if s[left] == t[right]:
                left += 1
            right +=1
            
        return left == n
        