class Solution:
    def maxProfit(self, prices, strategy, k):
        n = len(prices)

        # Base profit
        base_profit = 0
        for i in range(n):
            base_profit += strategy[i] * prices[i]

        # A[i] = original contribution
        # B[i] = contribution if forced to sell
        A = [strategy[i] * prices[i] for i in range(n)]
        B = [prices[i] - strategy[i] * prices[i] for i in range(n)]

        # Prefix sums
        prefA = [0] * (n + 1)
        prefB = [0] * (n + 1)
        for i in range(n):
            prefA[i + 1] = prefA[i] + A[i]
            prefB[i + 1] = prefB[i] + B[i]

        half = k // 2
        max_delta = 0

        for l in range(n - k + 1):
            mid = l + half
            r = l + k

            # First half: remove original contribution
            delta1 = -(prefA[mid] - prefA[l])

            # Second half: force sell
            delta2 = prefB[r] - prefB[mid]

            max_delta = max(max_delta, delta1 + delta2)

        return base_profit + max_delta
