from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_val = 0
        max_i = 0
        max_ik = 0

        for j in range(1, len(nums) - 1):
            max_i = max(max_i, nums[j - 1])
            max_ik = max(max_ik, max_i - nums[j])
            max_val = max(max_val, max_ik * nums[j + 1])

        return max_val
