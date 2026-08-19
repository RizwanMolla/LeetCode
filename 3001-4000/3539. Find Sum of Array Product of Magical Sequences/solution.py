from math import comb
from collections import defaultdict

MOD = 10**9 + 7

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        dp = defaultdict(int)
        dp[(0, 0, 0)] = 1  # (carry, ones, used)
        
        for val in nums:
            new_dp = defaultdict(int)
            for (carry, ones, used), total in dp.items():
                for cnt in range(m - used + 1):
                    next_used = used + cnt
                    next_carry = (carry + cnt) // 2
                    add_one = (carry + cnt) % 2
                    next_ones = ones + add_one
                    contribution = total * pow(val, cnt, MOD) % MOD * comb(m - used, cnt) % MOD
                    new_dp[(next_carry, next_ones, next_used)] = (new_dp[(next_carry, next_ones, next_used)] + contribution) % MOD
            dp = new_dp
        
        ans = 0
        for (carry, ones, used), val in dp.items():
            if used == m:
                ones += bin(carry).count("1")
                if ones == k:
                    ans = (ans + val) % MOD
        return ans
