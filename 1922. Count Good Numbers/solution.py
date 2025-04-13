class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def power(x, y):
            res = 1
            x %= MOD
            while y > 0:
                if y % 2:
                    res = (res * x) % MOD
                x = (x * x) % MOD
                y //= 2
            return res

        even_positions = (n + 1) // 2
        odd_positions = n // 2

        return (power(5, even_positions) * power(4, odd_positions)) % MOD
