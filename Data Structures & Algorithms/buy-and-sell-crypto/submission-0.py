class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        current = 0

        for i in range(1, len(prices)):

            diff = prices[i] - prices[i-1]

            current = max(0, current+diff)

            max_profit = max(current, max_profit)

        return max_profit        