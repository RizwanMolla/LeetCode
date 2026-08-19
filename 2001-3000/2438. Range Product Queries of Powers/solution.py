from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        # Step 1: Build powers array from bits of n
        powers = []
        bit = 1
        while n:
            if n & 1:
                powers.append(bit)
            n >>= 1
            bit <<= 1
        
        # Step 2: Precompute prefix products
        prefix = [1] * len(powers)
        prefix[0] = powers[0] % MOD
        for i in range(1, len(powers)):
            prefix[i] = (prefix[i-1] * powers[i]) % MOD
        
        # Step 3: Answer queries
        ans = []
        for l, r in queries:
            if l == 0:
                prod = prefix[r]
            else:
                prod = prefix[r] * pow(prefix[l-1], MOD-2, MOD) % MOD
            ans.append(prod)
        
        return ans
