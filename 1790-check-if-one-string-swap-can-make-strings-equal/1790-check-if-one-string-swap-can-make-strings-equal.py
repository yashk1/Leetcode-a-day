class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        if s1 == s2: return True
        
        bad = []
        for i in range(len(s1)):
            if s2[i] != s1[i]:
                bad.append([s1[i], s2[i]])
                
        if len(bad) == 2:
            if (bad[0][0] == bad[1][1] and bad[0][1] == bad[1][0]):
                return True
        return False

        
        
        
        