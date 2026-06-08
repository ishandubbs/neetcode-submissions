class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        #left = buy, right = sell

        while right < len(prices):
            #profitable ?
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else: 
                #might not be a profitable transaction
                left = right #if left is not < right, we set left to the minimum
            right += 1 #always updates regardless of conditions until right < len(prices)
        return max_profit