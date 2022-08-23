class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minp = prices[0]
        maxpr = 0
        
        for i in range(1, len(prices)):
            maxpr = max(maxpr , prices[i] - minp )
            minp = min(minp, prices[i])
        return maxpr