from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = min_sum = res = 0
        for num in nums:
            max_sum = max(0, max_sum + num)
            min_sum = min(0, min_sum + num)
            res = max(res, max_sum, -min_sum)
        return res
