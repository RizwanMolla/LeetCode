from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        last = [-1] * 32  # Track last seen index of each bit (0 to 31)

        for i in range(n - 1, -1, -1):
            num = nums[i]
            for bit in range(32):
                if (num >> bit) & 1:
                    last[bit] = i  # This bit is set at position i

            # We want the farthest position to the right that has a relevant bit
            max_len = 1
            for j in range(32):
                if last[j] != -1:
                    max_len = max(max_len, last[j] - i + 1)
            ans[i] = max_len

        return ans
