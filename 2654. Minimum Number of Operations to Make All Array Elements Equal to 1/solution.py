from math import gcd
from functools import reduce

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        total_gcd = reduce(gcd, nums)
        if total_gcd != 1:
            return -1
        
        count_ones = nums.count(1)
        if count_ones > 0:
            return n - count_ones
        
        min_len = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i+1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break
        
        return (min_len - 1) + (n - 1)
