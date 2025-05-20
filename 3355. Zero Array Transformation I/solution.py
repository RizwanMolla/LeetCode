from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)

        # Step 1: Apply difference array technique
        for l, r in queries:
            diff[l] += 1
            if r + 1 < n:
                diff[r + 1] -= 1

        # Step 2: Get prefix sum to find total allowed operations per index
        allowed = [0] * n
        curr = 0
        for i in range(n):
            curr += diff[i]
            allowed[i] = curr

        # Step 3: Check if we can reduce nums[i] to zero
        for i in range(n):
            if nums[i] > allowed[i]:
                return False

        return True
