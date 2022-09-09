class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        
        l = 0
        op = 0
        
        for r in range(len(s)):
            if s[r] not in seen:
                op = max(op, r-l+1)
            else:
                #it is not necessary if the elemtn is in seen, it can be part of a diff substring for that we will check by comapring left pointer with index of seenr
                if l > seen[s[r]]:
                    op = max(op, r-l+1)
                else:
                    l = seen[s[r]] + 1 #still confusing
                    
            seen[s[r]] = r
        return op
        
# abcabcbb- substring w/o repeating characters
#   ^

