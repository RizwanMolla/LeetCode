from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        total_distinct = len(set(nums))
        count = 0
        n = len(nums)
        
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                if len(seen) == total_distinct:
                    count += 1
        return count
