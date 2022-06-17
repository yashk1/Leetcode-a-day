class Solution:
    def fib(self, n: int) -> int:
        if n==0: return 0
        if n ==1: return 1
        
        cache = {}
        if n-1 not in cache:
            cache[n-1] = self.fib(n-1)
        if n-2 not in cache:
            cache[n-2] = self.fib(n-2)
        return cache[n-1] + cache[n-2]