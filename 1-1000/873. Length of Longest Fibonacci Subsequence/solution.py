from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {x: i for i, x in enumerate(arr)}
        n = len(arr)
        dp = {}
        max_len = 0

        for k in range(n):
            for j in range(k):
                i = index.get(arr[k] - arr[j])
                if i is not None and i < j:
                    dp[j, k] = dp.get((i, j), 2) + 1
                    max_len = max(max_len, dp[j, k])

        return max_len if max_len >= 3 else 0
