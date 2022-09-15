class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        mapping = {"(":')','[':']','{':'}' }
        
        
        for i in s:
            if i in mapping.keys():
                stack.append(i)
            elif stack and i == mapping[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []