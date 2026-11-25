class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        for r in range(len(prices)):
            if prices[r] <= prices[l]:
                l = r
            
            elif prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                if profit > max_profit:
                    max_profit = profit

        return max_profit
