from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        hashmap = Counter(secret)
        bulls = cows = 0
        for i, ch in enumerate(guess):
            if ch in hashmap:
                if ch == secret[i]:
                    bulls += 1

                    cows -= int (hashmap[ch] <=0)
                    
                else:
                    cows += int(hashmap[ch] >0)
                    
                hashmap[ch] -=1
        return "{}A{}B".format(bulls, cows)