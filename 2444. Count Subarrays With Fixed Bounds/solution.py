class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        res = 0
        lastMin = lastMax = lastInvalid = -1
        
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                lastInvalid = i
            if num == minK:
                lastMin = i
            if num == maxK:
                lastMax = i
            res += max(0, min(lastMin, lastMax) - lastInvalid)
        
        return res
