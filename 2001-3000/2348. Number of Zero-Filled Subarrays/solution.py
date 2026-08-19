from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        count = 0  # counts consecutive zeros
        for num in nums:
            if num == 0:
                count += 1
                result += count  # add new subarrays ending here
            else:
                count = 0
        return result
