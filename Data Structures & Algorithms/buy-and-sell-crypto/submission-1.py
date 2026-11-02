class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxSoFar = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
                r += 1
            else:
                maxSoFar = max(maxSoFar, profit)
                r += 1
        
        return maxSoFar