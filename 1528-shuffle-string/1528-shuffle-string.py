class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        t = [" "] * len(s)
        
        for i, char in enumerate(s):
            t[indices[i]] = char
        
        return "".join(t)