from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        
        total_sum_remainder = sum(nums) % p
        
        if total_sum_remainder == 0:
            return 0

        target_remainder = total_sum_remainder
        
        min_len = n 
        
        remainder_map = {0: -1}
        
        current_prefix_remainder = 0
        
        for i in range(n):
            current_prefix_remainder = (current_prefix_remainder + nums[i]) % p
            
            required_prev_remainder = (current_prefix_remainder - target_remainder + p) % p
            
            if required_prev_remainder in remainder_map:
                index_prev = remainder_map[required_prev_remainder]
                sub_len = i - index_prev
                min_len = min(min_len, sub_len)
            
            remainder_map[current_prefix_remainder] = i
            
        return min_len if min_len < n else -1