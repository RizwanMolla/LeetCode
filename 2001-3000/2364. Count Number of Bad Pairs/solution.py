from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        n = len(nums)
        freq = defaultdict(int)
        good_pairs = 0
        
        for i in range(n):
            transformed = nums[i] - i
            good_pairs += freq[transformed]
            freq[transformed] += 1
        
        total_pairs = n * (n - 1) // 2
        bad_pairs = total_pairs - good_pairs
        return bad_pairs