import math
from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        min_prefix_sum = [math.inf] * k
        
        min_prefix_sum[0] = 0
        
        current_sum = 0
        max_sum = -math.inf
        
        for i, num in enumerate(nums):
            current_sum += num
            
            remainder = (i + 1) % k
            
            if min_prefix_sum[remainder] != math.inf:
                max_sum = max(max_sum, current_sum - min_prefix_sum[remainder])
            
            min_prefix_sum[remainder] = min(min_prefix_sum[remainder], current_sum)
            
        return max_sum