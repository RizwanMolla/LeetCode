class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7
        maxLen = 14

        factorial = [1] * (n + maxLen + 1)
        inv_factorial = [1] * (n + maxLen + 1)

        for i in range(1, len(factorial)):
            factorial[i] = factorial[i-1] * i % MOD

        inv_factorial[-1] = pow(factorial[-1], MOD-2, MOD)
        for i in range(len(factorial)-2, -1, -1):
            inv_factorial[i] = inv_factorial[i+1] * (i+1) % MOD

        def nCr(a, b):
            if b > a or b < 0:
                return 0
            return factorial[a] * inv_factorial[b] % MOD * inv_factorial[a - b] % MOD

        from collections import defaultdict
        dp = defaultdict(lambda: [0] * (maxLen + 1))

        for v in range(1, maxValue + 1):
            dp[v][1] = 1

        for length in range(2, maxLen + 1):
            for v in range(1, maxValue + 1):
                for d in range(2, (maxValue // v) + 1):
                    dp[v * d][length] += dp[v][length - 1]
                    dp[v * d][length] %= MOD

        result = 0
        for val in range(1, maxValue + 1):
            for length in range(1, maxLen + 1):
                ways_to_choose_positions = nCr(n - 1, length - 1)
                result = (result + dp[val][length] * ways_to_choose_positions) % MOD

        return result