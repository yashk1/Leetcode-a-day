class Solution:
    
    def fib(self, n: int) -> int:
        dict = {} #this is memoized recursive

        if n == 0:
            return 0
        if n == 1:
            return 1
        
        if n-1 not in dict: dict[n-1] = self.fib(n-1)
        if n-2 not in dict: dict[n-2] = self.fib(n-2)
        
        return dict[n-1] + dict[n-2]
            