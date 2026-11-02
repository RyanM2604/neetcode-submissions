class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            # update profit if selling today gives a higher profit
            max_profit = max(max_profit, price - min_price)
            # update min_price if we find a cheaper price
            min_price = min(min_price, price)

        return max_profit
