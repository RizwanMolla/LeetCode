from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = [[0] * n for _ in range(k + 1)]

        for t in range(1, k + 1):
            best_buy = -prices[0]      # dp[t-1][j] - prices[j]
            best_sell = prices[0]      # dp[t-1][j] + prices[j]

            for i in range(1, n):
                # Either skip day i, or end a transaction here
                dp[t][i] = max(
                    dp[t][i - 1],
                    best_buy + prices[i],     # normal transaction
                    best_sell - prices[i]     # short selling transaction
                )

                # Update helpers
                best_buy = max(best_buy, dp[t - 1][i - 1] - prices[i])
                best_sell = max(best_sell, dp[t - 1][i - 1] + prices[i])

        return dp[k][n - 1]
