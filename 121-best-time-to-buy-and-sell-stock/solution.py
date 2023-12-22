class Solution:
    """You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
    def maxProfit(self, prices: list) -> int:
        buy_day = 0
        sell_day = 1
        profit = 0
  
        while sell_day < len(prices):
            if prices[buy_day] > prices[sell_day]:
                buy_day = sell_day
            else:
                current_profit = prices[sell_day] - prices[buy_day]
                profit = max(profit, current_profit)

            sell_day += 1

        return profit


s = Solution()

print(f'Max profit for [7,1,5,3,6,4] is {s.maxProfit([7,1,5,3,6,4])}')
print(f'Max profit for [7,6,4,3,1] is {s.maxProfit([7,6,4,3,1])}')
print(f'Max profit for [1,2] is {s.maxProfit([1,2])}')
print(f'Max profit for [1,1] is {s.maxProfit([1,1])}')
print(f'Max profit for [2,1] is {s.maxProfit([2,1])}')