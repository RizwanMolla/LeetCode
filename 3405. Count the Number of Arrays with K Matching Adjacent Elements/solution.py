MOD = 10**9 + 7
MAXN = 10**5 + 10

# Precompute factorials and inverse factorials
fact = [1] * MAXN
inv_fact = [1] * MAXN

for i in range(1, MAXN):
    fact[i] = fact[i - 1] * i % MOD
    inv_fact[i] = pow(fact[i], MOD - 2, MOD)

def combination(n: int, r: int) -> int:
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        # Choose k positions for adjacent matches
        # First element can be any of m values
        # Remaining n - k - 1 positions must be filled such that no match occurs: (m - 1) choices each
        total_ways = combination(n - 1, k) * m % MOD
        total_ways = total_ways * pow(m - 1, n - k - 1, MOD) % MOD
        return total_ways
