class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        primes = []
        is_prime = bytearray(b'\x01') * (n + 1)
        is_prime[0] = is_prime[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = 0

        for i in range(2, n + 1):
            if is_prime[i]:
                if s >= i:
                    primes.append(i)
                    s -= i
                else:
                    break

        return primes