from heapq import heappush, heappop
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        total_len = len(nums)
        group_size = total_len // 3

        prefix_sum = 0
        max_heap_prefix = []
        prefix_sums = [0] * (total_len + 1)

        for i, num in enumerate(nums[: 2 * group_size], 1):
            prefix_sum += num
            heappush(max_heap_prefix, -num)
            if len(max_heap_prefix) > group_size:
                prefix_sum -= -heappop(max_heap_prefix)
            prefix_sums[i] = prefix_sum

        suffix_sum = 0
        min_heap_suffix = []
        suffix_sums = [0] * (total_len + 1)

        for i in range(total_len, group_size, -1):
            num = nums[i - 1]
            suffix_sum += num
            heappush(min_heap_suffix, num)
            if len(min_heap_suffix) > group_size:
                suffix_sum -= heappop(min_heap_suffix)
            suffix_sums[i] = suffix_sum

        return min(
            prefix_sums[i] - suffix_sums[i + 1]
            for i in range(group_size, 2 * group_size + 1)
        )
