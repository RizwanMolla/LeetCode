class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Initialize 2D DP array
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Process each string
        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            
            # Update DP table backward
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])
        
        return dp[m][n]
