from math import ceil

class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        def can_divide(max_balls):
            ops = 0
            for n in nums:
                ops += ceil(n / max_balls) - 1
            return ops <= maxOperations

        l, r = 1, max(nums)
        res = r
        while l < r:
            m = l + ((r - l) // 2)
            if can_divide(m):
                r = m
                res = r
            else:
                l = m + 1
        return res