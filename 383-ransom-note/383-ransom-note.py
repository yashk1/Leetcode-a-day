from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        mc = collections.Counter(magazine)
        
        for i in ransomNote:
            if mc[i] <=0:
                return False
            mc[i] -=1
        return True
                