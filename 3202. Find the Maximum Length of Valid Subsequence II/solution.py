class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        max_len = 0
        for num in nums:
            mod = num % k
            for prev_mod in range(k):
                target_mod = (prev_mod - mod + k) % k
                dp[mod][target_mod] = dp[target_mod][mod] + 1
                max_len = max(max_len, dp[mod][target_mod])
        return max_len
