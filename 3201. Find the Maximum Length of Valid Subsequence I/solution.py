from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        MOD = 2
        dp = [[0] * MOD for _ in range(MOD)]
        
        max_length = 0
        
        for num in nums:
            parity = num % MOD
            for prev_parity in range(MOD):
                required_parity = (prev_parity - parity + MOD) % MOD
                dp[parity][required_parity] = dp[required_parity][parity] + 1
                max_length = max(max_length, dp[parity][required_parity])
        
        return max_length
