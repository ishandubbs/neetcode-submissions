class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])

                    # coin = 4
                    # a = 7
                    # dp[7] = 1 + dp[7 - 4] (dp[3])

        return dp[amount] if dp[amount] != amount + 1 else -1