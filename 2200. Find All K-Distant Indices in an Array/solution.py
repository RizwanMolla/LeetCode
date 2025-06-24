from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        result = set()

        # Step 1: Find all indices j where nums[j] == key
        for j in range(n):
            if nums[j] == key:
                # Step 2: Add all indices i such that |i - j| <= k
                start = max(0, j - k)
                end = min(n - 1, j + k)
                for i in range(start, end + 1):
                    result.add(i)

        # Return sorted list of unique indices
        return sorted(result)
