class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        dp = [1] * n
        parent = [-1] * n  

        max_len = 1
        max_idx = 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i

        result = []
        while max_idx != -1:
            result.append(nums[max_idx])
            max_idx = parent[max_idx]

        return result[::-1]
