from collections import Counter

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        freq = Counter(nums)
        max_len = 0

        for num in freq:
            if num + 1 in freq:
                max_len = max(max_len, freq[num] + freq[num + 1])

        return max_len
