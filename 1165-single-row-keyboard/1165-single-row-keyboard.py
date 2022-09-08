class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hashm = {}
        
        for i, char in enumerate(keyboard):
            hashm[char] = i
        
        sum=0
        prev = 0
        for i in word:
            sum += abs(hashm[i]-prev)
            prev = hashm[i]
            
        return sum