class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0

        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]

            if prices[r] < prices[l]:
                l = r
            
            maxProfit = max(maxProfit, profit)
        
        return maxProfit