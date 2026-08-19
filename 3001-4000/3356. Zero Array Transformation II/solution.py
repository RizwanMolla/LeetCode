from typing import List
from bisect import bisect_left

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def isZeroArrayPossible(queryCount: int) -> bool:
            prefixDiff = [0] * (len(nums) + 1)
            for start, end, decrement in queries[:queryCount]:
                prefixDiff[start] += decrement
                prefixDiff[end + 1] -= decrement
            cumulativeSum = 0
            for num, delta in zip(nums, prefixDiff):
                cumulativeSum += delta
                if num > cumulativeSum:
                    return False
            return True

        totalQueries = len(queries)
        minQueriesRequired = bisect_left(range(totalQueries + 1), True, key=isZeroArrayPossible)
        return -1 if minQueriesRequired > totalQueries else minQueriesRequired
