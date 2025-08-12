class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Precompute powers
        powers = []
        i = 1
        while (val := i ** x) <= n:
            powers.append(val)
            i += 1
        
        # Step 2: Bottom-up DP
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        
        for p in powers:
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % MOD
        
        return dp[n]
