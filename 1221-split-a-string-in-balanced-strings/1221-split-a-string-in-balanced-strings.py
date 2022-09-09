class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = count = 0
        
        for i in s:
            if i == 'R': count+=1
            if i == 'L': count -=1
            if count== 0: res+=1
        
        return res
# constraint-> the string is balanced