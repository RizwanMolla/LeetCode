class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        @cache
        def dfs(i, a, b):
            if i == len(nums): return a == b
            return (
                dfs(i + 1, a, b) +
                dfs(i + 1, gcd(a, nums[i]), b) +  
                dfs(i + 1, a, gcd(b, nums[i]))
            ) % (10 ** 9 + 7)
        return dfs(0, 0, 0) - 1