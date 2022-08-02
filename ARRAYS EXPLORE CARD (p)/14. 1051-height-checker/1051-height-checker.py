from collections import Counter

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        counter = Counter(heights)
        
        i = 0
        count = 0 
        for h in heights:
            while counter[i] == 0:
                i+=1
                
            if i != h:
                count +=1
                
            counter[i] -=1
        return count
        
        