class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1 # base case
       
        for coin in coins:
            for a in range(coin, amount + 1):
                    dp[a] += dp[a - coin]

                    # coin = 4
                    # a = 7
                    # dp[7] = 1 + dp[7 - 4] (dp[3])

        return dp[amount]
