class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        if any(num < k for num in nums):
            return -1

        greater_than_k = set()

        for num in nums:
            if num > k:
                greater_than_k.add(num)

        return len(greater_than_k)