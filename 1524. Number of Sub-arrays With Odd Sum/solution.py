from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd, even, prefix_sum, res, mod = 0, 1, 0, 0, 10**9 + 7

        for num in arr:
            prefix_sum += num
            if prefix_sum % 2:
                res += even
                odd += 1
            else:
                res += odd
                even += 1

        return res % mod