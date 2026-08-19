from collections import defaultdict

class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        left = 0
        freq = defaultdict(int)
        pair_count = 0
        res = 0

        for right in range(len(nums)):
            pair_count += freq[nums[right]]
            freq[nums[right]] += 1

            while pair_count >= k:
                res += len(nums) - right
                freq[nums[left]] -= 1
                pair_count -= freq[nums[left]]
                left += 1

        return res
