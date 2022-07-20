class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        s2 = []
        
        for i in s:
            if i == '#':
                if s1:
                    s1.pop()
                    
            else:
                s1.append(i)
                
        for i in t:
            if i == '#':
                if s2:
                    s2.pop()
            else:
                s2.append(i)
        
        return s1 == s2
    
#Time: O(M + N), where M <= 200 is length of string s, N <= 200 is length of string t.
#Space: O(M + N)
