class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        length = len(piles)
        dp = [[0] * length for _ in range(length)]

        for index, stones in enumerate(piles):
            dp[index][index] = stones

        for left in range(length - 2, -1, -1):
            for right in range(left + 1, length):
                dp[left][right] = max(
                    piles[left] - dp[left + 1][right],
                    piles[right] - dp[left][right - 1]
                )

        return dp[0][length - 1] > 0