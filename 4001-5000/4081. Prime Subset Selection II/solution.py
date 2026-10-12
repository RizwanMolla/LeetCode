class Solution:
    def maxPrimeSubset(self, n: int, s: int) -> list[int]:
        isPrime = bytearray(b'\x01') * (n + 1)
        isPrime[0] = isPrime[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                isPrime[i * i:n + 1:i] = b'\x00' * (((n - i * i) // i) + 1)

        primeNums = [i for i in range(2, n + 1) if isPrime[i] and i <= s]
        dp = [None] * (s + 1)
        dp[0] = ()

        for p in primeNums:
            for total in range(s, p - 1, -1):
                if dp[total - p] is not None:
                    candidate = dp[total - p] + (p,)
                    current = dp[total]

                    if current is None or len(candidate) < len(current) or (len(candidate) == len(current) and candidate < current):
                        dp[total] = candidate

        for total in range(s, 0, -1):
            if dp[total] is not None:
                return list(dp[total])

        return []