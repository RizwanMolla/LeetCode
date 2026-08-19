class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        neg_count = sum(1 for x in nums if x < 0)
        pos_count = sum(1 for x in nums if x > 0)
        return max(neg_count, pos_count)
